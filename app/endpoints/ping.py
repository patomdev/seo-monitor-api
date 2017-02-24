from flask import Blueprint, jsonify

blueprint = Blueprint('ping', __name__)

@blueprint.route("/ping")
def get():
    return jsonify({'msg': 'ok'}), 200
