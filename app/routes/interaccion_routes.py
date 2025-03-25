from flask import Blueprint, request, jsonify
from app.services.interaccion_servise import get_interacciones, create_interaccion
from app.schemas.interaccion_schema import InteraccionSchema

interaccion_bp = Blueprint("interaccion", __name__)
interaccion_schema = InteraccionSchema()
interacciones_schema = InteraccionSchema(many=True)


@interaccion_bp.route("/interacciones", methods=["GET"])
def interacciones():
    interacciones = get_interacciones()
    return jsonify(interacciones_schema.dump(interacciones))


@interaccion_bp.route("/interacciones", methods=["POST"])
def add_interaccion():
    new_interaccion = create_interaccion(request.json)
    return jsonify(interaccion_schema.dump(new_interaccion)), 201
