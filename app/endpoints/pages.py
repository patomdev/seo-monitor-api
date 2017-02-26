from flask import Blueprint, jsonify
from webargs import fields, flaskparser
from app.db import get_db
from .. import __version__

blueprint = Blueprint(
    'pages',
    __name__,
    url_prefix='/' + __version__ + '/pages/'
)

FILTER = {
    'url': fields.Str(required=True),
    'title': fields.Str()
}

@blueprint.route('<int:id>')
@blueprint.route('', defaults={'id': 0})
def get(id):
    return jsonify({'id': id})

@blueprint.route('', methods=['POST'])
@flaskparser.use_kwargs(FILTER)
def post(url, title):
    db = get_db()
    db['pages'].insert_one({'url': url, 'title': title})

    return jsonify({'status': 'ok'}), 201

@blueprint.route('<int:id>', methods=['PUT'])
@flaskparser.use_kwargs(FILTER)
def put(id, url, title):
    return jsonify({'id': id, 'url': url, 'title': title})
