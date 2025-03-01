from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from src.controllers.agents_controller import get_all

main = Blueprint("agents_blueprint", __name__)


@main.route("/", methods=["GET"])
def get_all_agents():
    return get_all()


@main.errorhandler(ValidationError)
def handle_marshmallow_validation_error(error):
    return jsonify(error.messages), 400
