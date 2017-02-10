"""Structures for serializing"""

from marshmallow import Schema, fields

class MSAA_Schema(Schema):
    class Meta:
        # TODO Convert pointer to object for serialization
        # parent = fields.Nested('self')
        fields = ("name", "role", "state", "value")
        exclude = ("_target", )
