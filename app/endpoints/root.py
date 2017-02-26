from flask import Blueprint, jsonify
from .. import __version__
from ._utils import route

blueprint = Blueprint('root', __name__)


@blueprint.route('/api')
def get():
    data = dict()
    data['sites'] = route('sites.get', _external=True)
    data['version'] = __version__
    return jsonify(data)


@blueprint.route('/ping')
def handle_checks():
    return jsonify({'msg': 'ok'}), 200
