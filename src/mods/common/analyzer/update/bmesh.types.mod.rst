.. mod-type:: update

.. module:: bmesh.types

.. class:: BMLayerCollection

   .. base-class:: typing.Generic[GenericType1]

      :mod-option base-class: skip-refine

   .. attribute:: active

      :type: :class:`bmesh.types.BMLayerItem`\ [GenericType1]
      :mod-option attribute: skip-refine

   .. method:: get(key, default=None)

      :type default: GenericType2
      :mod-option arg default: skip-refine

   .. method:: items()

      :rtype: list[str, :class:`bmesh.types.BMLayerItem`\ [GenericType1]]
      :mod-option rtype: skip-refine

   .. method:: new()

      :rtype: :class:`bmesh.types.BMLayerItem`\ [GenericType1]
      :mod-option rtype: skip-refine

   .. method:: remove(layer)

      :type layer: :class:`bmesh.types.BMLayerItem`\ [GenericType1]
      :mod-option arg layer: skip-refine

   .. method:: values()

      :rtype: list[:class:`bmesh.types.BMLayerItem`\ [GenericType1]]
      :mod-option rtype: skip-refine

   .. method:: verify()

      :rtype: :class:`bmesh.types.BMLayerItem`\ [GenericType1]
      :mod-option rtype: skip-refine

.. class:: BMLayerItem

   .. base-class:: typing.Generic[GenericType1]

      :mod-option base-class: skip-refine

.. class:: BMVert

   .. method:: copy_from(other)

      :type other: :class:`BMVert`

.. class:: BMEdge

   .. method:: copy_from(other)

      :type other: :class:`BMEdge`

.. class:: BMFace

   .. method:: copy_from(other)

      :type other: :class:`BMFace`

.. class:: BMLoop

   .. method:: copy_from(other)

      :type other: :class:`BMLoop`
