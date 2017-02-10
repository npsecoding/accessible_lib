"""Structures for serializing"""

from marshmallow import Schema, fields

class MSAA_Schema(Schema):
    class Meta:
        parent = fields.Nested('self')
        children = fields.Nested('self', many=True)
        fields = ("name", "children", "role", "parent", "state", "value")
        exclude = ("_target", )
