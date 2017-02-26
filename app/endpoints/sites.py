from flask import Blueprint, jsonify
from webargs import fields, flaskparser
from bson.json_util import dumps
from app.db import get_db
from .. import __version__

blueprint = Blueprint(
    'sites',
    __name__,
    url_prefix='/' + __version__ + '/sites/'
)

FILTER = {
    'url': fields.Str(required=True),
    'title': fields.Str()
}

@blueprint.route('<int:id>')
@blueprint.route('', defaults={'id': 0})
def get(id):
    return jsonify({'id': id})

@blueprint.route('/')
def get_list():
    db = get_db()
    sites = db['sites'].find({})
    return dumps(sites)

@blueprint.route('', methods=['POST'])
@flaskparser.use_kwargs(FILTER)
def post(url, title):
    db = get_db()
    db['sites'].insert_one({'url': url, 'title': title})

    return jsonify({'status': 'ok'}), 201

@blueprint.route('<int:id>', methods=['PUT'])
@flaskparser.use_kwargs(FILTER)
def put(id, url, title):
    return jsonify({'id': id, 'url': url, 'title': title})
