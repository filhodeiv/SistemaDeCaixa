from flask import Blueprint, current_app, request, jsonify
from .models import Caixa
from .serealizer import CaixaSchema


bp_caixa = Blueprint('caaixa', __name__)


@bp_caixa.route('/mostrar', methods=['GET'])
def mostrar():
    result = Caixa.query.all()
    return CaixaSchema(many=True).jsonify(result), 200


@bp_caixa.route('/deletar/<identificador>', methods=['GET'])
def deletar(identificador):
    Caixa.query.filter(Caixa.id_pagamento == identificador).delete()
    current_app.db.session.commit()
    return jsonify('Deletado!!!!')


@bp_caixa.route('/modificar/<identificador>', methods=['POST'])
def modificar(identificador):
    bs = CaixaSchema()
    query = Caixa.query.filter(Caixa.id_pagamento == identificador)
    query.update(request.json)
    current_app.db.session.commit()
    return bs.jsonify(query.first())


@bp_caixa.route('/transacao', methods=['POST'])
def transacao():

    bs = CaixaSchema()
    caixa, error = bs.load(request.json)

    if error:
        return jsonify(error), 401

    valor_pago = request.POST['valor_pago']
    valor_produto = request.POST['valor_produto']
    troco = valor_pago - valor_produto
    cedula = 100
    total_de_cedulas = 0

    while True:

        if troco >= cedula:
            troco -= cedula
            total_de_cedulas += 1

        else:
            if cedula == 100:
                cedula = 50

            elif cedula == 50:
                cedula = 20

            elif cedula == 20:
                cedula = 10

            elif cedula == 10:
                cedula = 5

            elif cedula == 5:
                cedula = 2

    current_app.db.session.add(caixa)
    current_app.db.session.commit()
    return bs.jsonify(caixa), 201
