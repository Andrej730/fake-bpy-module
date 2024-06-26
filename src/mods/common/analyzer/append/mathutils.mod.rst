.. mod-type:: append

.. module:: mathutils

.. class:: Color

   .. method:: __init__(rgb=(0.0, 0.0, 0.0))

   .. method:: __add__(other)

      :type other: :class:`Color`
      :rtype: :class:`Color`

   .. method:: __sub__(other)

      :type other: :class:`Color`
      :rtype: :class:`Color`

   .. method:: __mul__(other)

      :type other: int, float
      :rtype: :class:`Color`

   .. method:: __truediv__(other)

      :type other: int, float
      :rtype: :class:`Color`

   .. method:: __radd__(other)

      :type other: :class:`Color`
      :rtype: :class:`Color`

   .. method:: __rsub__(other)

      :type other: :class:`Color`
      :rtype: :class:`Color`

   .. method:: __rmul__(other)

      :type other: int, float
      :rtype: :class:`Color`

   .. method:: __rtruediv__(other)

      :type other: int, float
      :rtype: :class:`Color`

   .. method:: __iadd__(other)

      :type other: :class:`Color`
      :rtype: :class:`Color`

   .. method:: __isub__(other)

      :type other: :class:`Color`
      :rtype: :class:`Color`

   .. method:: __imul__(other)

      :type other: int, float
      :rtype: :class:`Color`

   .. method:: __itruediv__(other)

      :type other: int, float
      :rtype: :class:`Color`

   .. method:: __getitem__(key)

      :type key: int
      :rtype: float

.. class:: Euler

   .. method:: __init__(angles=(0.0, 0.0, 0.0), order='XYZ')

   .. method:: __getitem__(key)

      :type key: int
      :rtype: float

.. class:: Matrix

   .. method:: __init__(rows=((1.0, 0.0, 0.0, 0.0), (0.0, 1.0, 0.0, 0.0), (0.0, 0.0, 1.0, 0.0), (0.0, 0.0, 0.0, 1.0)))

   .. method:: __getitem__(key)

      :type key: int
      :rtype: :class:`Vector`

   .. method:: __len__()

      :rtype: int

   .. method:: __add__(other)

      :type other: :class:`Matrix`
      :rtype: :class:`Matrix`

   .. method:: __sub__(other)

      :type other: :class:`Matrix`
      :rtype: :class:`Matrix`

   .. method:: __mul__(other)

      :type other: int, float
      :rtype: :class:`Matrix`

   .. method:: __matmul__(other)

      :type other: :class:`Matrix`
      :rtype: :class:`Matrix`
      :option function: overload

   .. method:: __matmul__(other)

      :type other: :class:`Vector`
      :rtype: :class:`Vector`
      :option function: overload

   .. method:: __matmul__(other)

      :type other: :class:`Matrix`, :class:`Vector`
      :rtype: :class:`Matrix`, :class:`Vector`

   .. method:: __radd__(other)

      :type other: :class:`Matrix`
      :rtype: :class:`Matrix`

   .. method:: __rsub__(other)

      :type other: :class:`Matrix`
      :rtype: :class:`Matrix`

   .. method:: __rmul__(other)

      :type other: int, float
      :rtype: :class:`Matrix`

   .. method:: __imul__(other)

      :type other: int, float
      :rtype: :class:`Matrix`

.. class:: Quaternion

   .. method:: __init__(seq=(1.0, 0.0, 0.0, 0.0))

   .. method:: __len__()

      :rtype: int

   .. method:: __getitem__(key)

      :type key: int
      :rtype: float

   .. method:: __setitem__(key, value)

      :type key: int
      :type value: float
      :rtype: float

   .. method:: __add__(other)

      :type other: :class:`Quaternion`
      :rtype: :class:`Quaternion`

   .. method:: __sub__(other)

      :type other: :class:`Quaternion`
      :rtype: :class:`Quaternion`

   .. method:: __mul__(other)

      :type other: int, float, :class:`Quaternion`
      :rtype: :class:`Quaternion`

   .. method:: __matmul__(other)

      :type other: :class:`Quaternion`
      :rtype: :class:`Quaternion`
      :option function: overload

   .. method:: __matmul__(other)

      :type other: :class:`Vector`
      :rtype: :class:`Vector`
      :option function: overload

   .. method:: __matmul__(other)

      :type other: :class:`Vector`, :class:`Quaternion`
      :rtype: :class:`Vector`, :class:`Quaternion`

   .. method:: __radd__(other)

      :type other: :class:`Quaternion`
      :rtype: :class:`Quaternion`

   .. method:: __rsub__(other)

      :type other: :class:`Quaternion`
      :rtype: :class:`Quaternion`

   .. method:: __rmul__(other)

      :type other: int, float, :class:`Quaternion`
      :rtype: :class:`Quaternion`

   .. method:: __imul__(other)

      :type other: int, float, :class:`Quaternion`
      :rtype: :class:`Quaternion`

.. class:: Vector

   .. method:: __init__(seq=(0.0, 0.0, 0.0))

   .. method:: __len__()

      :rtype: int

   .. method:: __getitem__(key)

      :type key: int
      :rtype: float

   .. method:: __setitem__(key, value)

      :type key: int
      :type value: float
      :rtype: float

   .. method:: __neg__()

      :rtype: :class:`Vector`

   .. method:: __add__(other)

      :type other: :class:`Vector`
      :rtype: :class:`Vector`

   .. method:: __sub__(other)

      :type other: :class:`Vector`
      :rtype: :class:`Vector`

   .. method:: __mul__(other)

      :type other: int, float
      :rtype: :class:`Vector`

   .. method:: __truediv__(other)

      :type other: int, float
      :rtype: :class:`Vector`

   .. method:: __matmul__(other)

      :type other: :class:`Vector`
      :rtype: float
      :option function: overload

   .. method:: __matmul__(other)

      :type other: :class:`Matrix`
      :rtype: :class:`Vector`
      :option function: overload

   .. method:: __matmul__(other)

      :type other: :class:`Vector`, :class:`Matrix`
      :rtype: :class:`Vector`, float

   .. method:: __radd__(other)

      :type other: :class:`Vector`
      :rtype: :class:`Vector`

   .. method:: __rsub__(other)

      :type other: :class:`Vector`
      :rtype: :class:`Vector`

   .. method:: __rmul__(other)

      :type other: int, float
      :rtype: :class:`Vector`

   .. method:: __rtruediv__(other)

      :type other: int, float
      :rtype: :class:`Vector`

   .. method:: __iadd__(other)

      :type other: :class:`Vector`
      :rtype: :class:`Vector`

   .. method:: __isub__(other)

      :type other: :class:`Vector`
      :rtype: :class:`Vector`

   .. method:: __imul__(other)

      :type other: int, float
      :rtype: :class:`Vector`

   .. method:: __itruediv__(other)

      :type other: int, float
      :rtype: :class:`Vector`
