"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

import cStringIO as StringIO
import struct

class takktile_t(object):
    __slots__ = ["numSensors", "pressure", "temperature"]

    def __init__(self):
        self.numSensors = 0
        self.pressure = []
        self.temperature = []

    def encode(self):
        buf = StringIO.StringIO()
        buf.write(takktile_t._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">i", self.numSensors))
        buf.write(struct.pack('>%df' % self.numSensors, *self.pressure[:self.numSensors]))
        buf.write(struct.pack('>%df' % self.numSensors, *self.temperature[:self.numSensors]))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = StringIO.StringIO(data)
        if buf.read(8) != takktile_t._get_packed_fingerprint():
            raise ValueError("Decode error")
        return takktile_t._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = takktile_t()
        self.numSensors = struct.unpack(">i", buf.read(4))[0]
        self.pressure = struct.unpack('>%df' % self.numSensors, buf.read(self.numSensors * 4))
        self.temperature = struct.unpack('>%df' % self.numSensors, buf.read(self.numSensors * 4))
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if takktile_t in parents: return 0
        tmphash = (0x3c3a9068bc68b556) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff)  + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if takktile_t._packed_fingerprint is None:
            takktile_t._packed_fingerprint = struct.pack(">Q", takktile_t._get_hash_recursive([]))
        return takktile_t._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

