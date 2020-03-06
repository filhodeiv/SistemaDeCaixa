from marshmallow import fields, validates, ValidationError
from flask_marshmallow import Marshmallow
from .models import Caixa

ma = Marshmallow()


def configure(app):
    ma.init_app(app)


class CaixaSchema(ma.ModelSchema):
    class Meta:
        model = Caixa

    valor_pago = fields.Str(required=True)
    valor_produto = fields.Str(required=True)
