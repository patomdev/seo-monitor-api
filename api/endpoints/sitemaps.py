from flask import Blueprint, jsonify
from webargs import fields, flaskparser
from api.db import get_db

blueprint = Blueprint('sitemaps', __name__, url_prefix='/api/sitemap/')

FILTER = {
    'url': fields.Str(required=True),
    'title': fields.Str()
}

@blueprint.route('<int:id>')
def get_by_id(id):
    return jsonify({'id': id})

@blueprint.route('', methods=['POST'])
@flaskparser.use_kwargs(FILTER)
def post(url, title):
    db = get_db()
    db['posts'].insert_one({'url': url, 'title': title})

    return jsonify({'status': 'ok'}), 201

@blueprint.route('<int:id>', methods=['PUT'])
@flaskparser.use_kwargs(FILTER)
def put(id, url, title):
    return jsonify({'id': id, 'url': url, 'title': title})
