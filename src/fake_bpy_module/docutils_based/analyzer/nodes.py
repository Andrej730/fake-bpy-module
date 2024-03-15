from typing import TypeVar, Type
from docutils import nodes

T = TypeVar("T", bound=nodes.Node)


class NodeBase(nodes.Element):
    def append_child(self, item: nodes.Node):
        self.insert(len(self.children), item)


class UniqueElementNode(NodeBase):
    # pylint: disable=W1113
    def __init__(self, rawsource: str = "", *children: nodes.Node,
                 **attributes):
        super().__init__(rawsource, *children, **attributes)

        self.elements = {}

    def append_child(self, item: nodes.Node):
        self.insert(len(self.children), item)
        self.elements[type(item)] = item

    def element(self, element_type: Type[T]) -> T:
        return self.elements[element_type]


class ListNode(NodeBase, nodes.Sequential):
    def empty(self) -> bool:
        return len(self.children) == 0


class TextNode(nodes.TextElement):
    def add_text(self, text: str):
        self.insert(len(self.children), nodes.Text(text))


class AttributeListNode(ListNode):
    tagname = "attribute-list"
    child_text_separator = ""


class FunctionListNode(ListNode):
    tagname = "function-list"
    child_text_separator = ""


class NameNode(TextNode, nodes.Part):
    tagname = "name"
    child_text_separator = ""


class DataTypeListNode(ListNode):
    tagname = "data-type-list"
    child_text_separator = ""


class DataTypeNode(TextNode, nodes.Part):
    tagname = "data-type"
    child_text_separator = ""


class DescriptionNode(TextNode, nodes.Part):
    tagname = "description"
    child_text_separator = ""

    def empty(self) -> bool:
        return len(self.children) == 0


class DataNode(UniqueElementNode, nodes.Part):
    tagname = "data"
    child_text_separator = ""

    # pylint: disable=W1113
    @classmethod
    def create_template(cls, rawsource: str = "", *children: nodes.Node,
                        **attributes) -> "DataNode":
        node = DataNode(rawsource, *children, **attributes)

        node.append_child(NameNode())
        node.append_child(DescriptionNode())
        node.append_child(DataTypeListNode())

        return node


class AttributeNode(DataNode):
    tagname = "attribute"
    child_text_separator = ""

    # pylint: disable=W1113
    @classmethod
    def create_template(cls, rawsource: str = "", *children: nodes.Node,
                        **attributes) -> "AttributeNode":
        node = AttributeNode(rawsource, *children, **attributes)

        node.append_child(NameNode())
        node.append_child(DescriptionNode())
        node.append_child(DataTypeListNode())

        return node


class DefaultValueNode(TextNode, nodes.Part):
    tagname = "default-value"
    child_text_separator = ""

    def empty(self) -> bool:
        return len(self.children) == 0


class ArgumentListNode(ListNode):
    tagname = "argument-list"
    child_text_separator = ""


class ArgumentNode(UniqueElementNode, nodes.Part):
    tagname = "argument"
    child_text_separator = ""

    # pylint: disable=W1113
    @classmethod
    def create_template(cls, rawsource: str = "", *children: nodes.Node,
                        **attributes) -> "ArgumentNode":
        node = ArgumentNode(rawsource, *children, **attributes)

        node.append_child(NameNode())
        node.append_child(DescriptionNode())
        node.append_child(DefaultValueNode())
        node.append_child(DataTypeListNode())

        return node


class FunctionReturnNode(UniqueElementNode, nodes.Part):
    tagname = "return"
    child_text_separator = ""

    # pylint: disable=W1113
    @classmethod
    def create_template(cls, rawsource: str = "", *children: nodes.Node,
                        **attributes) -> "FunctionReturnNode":
        node = FunctionReturnNode(rawsource, *children, **attributes)

        node.append_child(DescriptionNode())
        node.append_child(DataTypeListNode())

        return node

    def empty(self) -> bool:
        for child in self.children:
            if not child.empty():
                return False
        return True


class FunctionNode(UniqueElementNode, nodes.Part):
    tagname = "function"
    child_text_separator = ""

    # pylint: disable=W1113
    @classmethod
    def create_template(cls, rawsource: str = "", *children: nodes.Node,
                        **attributes) -> "FunctionNode":
        node = FunctionNode(rawsource, *children, **attributes)

        node.append_child(NameNode())
        node.append_child(DescriptionNode())
        node.append_child(ArgumentListNode())
        node.append_child(FunctionReturnNode.create_template())

        return node


class BaseClassListNode(ListNode):
    tagname = "base-class-list"
    child_text_separator = ""


class BaseClassNode(UniqueElementNode, nodes.Part):
    tagname = "base-class"
    child_text_separator = ""

    # pylint: disable=W1113
    @classmethod
    def create_template(cls, rawsource: str = "", *children: nodes.Node,
                        **attributes) -> "BaseClassNode":
        node = BaseClassNode(rawsource, *children, **attributes)

        node.append_child(DataTypeListNode())

        return node


class ClassNode(UniqueElementNode, nodes.Part):
    tagname = "class"
    child_text_separator = ""

    # pylint: disable=W1113
    @classmethod
    def create_template(cls, rawsource: str = "", *children: nodes.Node,
                        **attributes) -> "ClassNode":
        node = ClassNode(rawsource, *children, **attributes)

        node.append_child(NameNode())
        node.append_child(DescriptionNode())
        node.append_child(BaseClassListNode())
        node.append_child(AttributeListNode())
        node.append_child(FunctionListNode())

        return node


class ModuleNode(UniqueElementNode, nodes.Part):
    tagname = "module"
    child_text_separator = ""

    # pylint: disable=W1113
    @classmethod
    def create_template(cls, rawsource: str = "", *children: nodes.Node,
                        **attributes) -> "ModuleNode":
        node = ModuleNode(rawsource, *children, **attributes)

        node.append_child(NameNode())
        node.append_child(DescriptionNode())

        return node


class CodeNode(TextNode, nodes.Part):
    tagname = "code"
    child_text_separator = ""


class ModTypeNode(TextNode, nodes.Part):
    tagname = "mod-type"
    child_text_separator = ""


class CodeDocumentNode(TextNode, nodes.Part):
    tagname = "code-document"
    child_text_separator = ""
