from flask_sqlalchemy import SQLAlchemy
# from passlib.hash import pbkdf2_sha256

db = SQLAlchemy()


def configure(app):
    db.init_app(app)
    app.db = db


class caixa(db.Model):
    id_pagamento = db.Column(db.Integer, primary_key=True)
    cedula = db.Column(db.Integer)
    moeda = db.Column(db.Integer)
    valor_pago = db.Column(db.Integer)
    valor_produto = db.Column(db.Integer)
    troco = db.Column(db.Integer)
