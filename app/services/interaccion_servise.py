from app import db
from app.models.interaccion import Interaccion


def get_interacciones():
    return Interaccion.query.all()


def create_interaccion(interaccion):
    new_interaccion = Interaccion(
        elemento=interaccion["elemento"],
        usuario_cookie=interaccion["usuario_cookie"],
    )
    db.session.add(new_interaccion)
    db.session.commit()
    return new_interaccion
