"""autogenerated by genpy from ax2550/Encoders.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class Encoders(genpy.Message):
  _md5sum = "265d820a2b35c4bff51c4a1d293ad5c0"
  _type = "ax2550/Encoders"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """float32 time_delta # Time since last encoder update.
int32 left_wheel  # Encoder counts (absolute or relative)
int32 right_wheel # Encoder counts (absolute or relative)

"""
  __slots__ = ['time_delta','left_wheel','right_wheel']
  _slot_types = ['float32','int32','int32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       time_delta,left_wheel,right_wheel

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Encoders, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.time_delta is None:
        self.time_delta = 0.
      if self.left_wheel is None:
        self.left_wheel = 0
      if self.right_wheel is None:
        self.right_wheel = 0
    else:
      self.time_delta = 0.
      self.left_wheel = 0
      self.right_wheel = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_f2i.pack(_x.time_delta, _x.left_wheel, _x.right_wheel))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 12
      (_x.time_delta, _x.left_wheel, _x.right_wheel,) = _struct_f2i.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_f2i.pack(_x.time_delta, _x.left_wheel, _x.right_wheel))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 12
      (_x.time_delta, _x.left_wheel, _x.right_wheel,) = _struct_f2i.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_f2i = struct.Struct("<f2i")
