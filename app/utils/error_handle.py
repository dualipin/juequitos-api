from flask import jsonify


def handle_error(error):
    response = {"error": str(error), "message": "Ha ocurrido un error"}

    return jsonify(response), 500
