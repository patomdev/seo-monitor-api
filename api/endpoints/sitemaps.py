from flask import Blueprint, jsonify
from webargs import fields, flaskparser

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
    return jsonify({'url': url, 'title': title})

@blueprint.route('<int:id>', methods=['PUT'])
@flaskparser.use_kwargs(FILTER)
def put(id, url, title):
    return jsonify({'id': id, 'url': url, 'title': title})