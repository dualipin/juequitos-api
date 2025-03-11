from flask import Flask, request, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy
import datetime
import uuid
from flask_cors import CORS

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///interacciones.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

CORS(
    app,
    resources={r"/*": {"origins": ["http://localhost:5174", "http://localhost:5173"]}},
)


class Interaccion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    elemento = db.Column(db.String(20), nullable=False)
    fecha = db.Column(db.DateTime, default=datetime.datetime.now)

    def to_dict(self):
        return {"id": self.id, "elemento": self.elemento, "fecha": self.fecha}


@app.route("/interaccion", methods=["POST"])
def registrar_interaccion():
    data = request.json
    if not data or not data.get("elemento"):
        return jsonify({"error": "Elemento is required"}), 400

    try:
        nueva_interaccion = Interaccion(elemento=data["elemento"])
        db.session.add(nueva_interaccion)
        db.session.commit()
        return jsonify({"message": "Interacción registrada"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@app.route("/track", methods=["POST"])
def track_user():
    user_id = request.cookies.get("user_id") or str(uuid.uuid4())
    resp = make_response("Tracking user")
    resp.set_cookie("user_id", user_id)
    return resp


@app.route("/api/interacciones", methods=["GET"])
def obtener_interacciones():
    try:
        datos = Interaccion.query.all()
        return jsonify({"data": [i.to_dict() for i in datos]}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
