from marshmallow import Schema, fields


class InteraccionSchema(Schema):
    id = fields.Int(dump_only=True)
    elemento = fields.Str(required=True)
    fecha = fields.DateTime(dump_only=True)
    usuario_cookie = fields.Str(required=True)
