from app import db
import datetime


class Interaccion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    elemento = db.Column(db.String(20), nullable=False)
    fecha = db.Column(db.DateTime, default=datetime.datetime.now)
    usuario_cookie = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "elemento": self.elemento,
            "fecha": self.fecha,
            "usuario_cookie": self.usuario_cookie,
        }
