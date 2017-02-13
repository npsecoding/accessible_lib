"""Structures for serializing"""

from marshmallow import Schema, fields

class MSAA_Schema(Schema):
    """MSAA Accesible serialization format"""
    class Meta:
        parent = fields.Nested('self')
        children = fields.Nested('self', many=True)
        fields = ("name", "childcount", "children", "role", "parent", "state", "value")
        exclude = ("_target", )

# TODO
# class IA2_Schema(Schema):
#     """IA2 Accesible serialization format"""
#     class Meta:

# TODO
# class ATK_Schema(Schema):
#     """ATK Accesible serialization format"""
#     class Meta:

# TODO
# class ATSPI_Schema(Schema):
#     """ATSPI Accesible serialization format"""
#     class Meta:
