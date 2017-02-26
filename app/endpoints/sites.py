import pymongo
from flask import Blueprint, jsonify
from webargs import fields, flaskparser
from bson.json_util import dumps
from bson.objectid import ObjectId
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

def normalize(siteDoc):
    return {
        'id': str(ObjectId(siteDoc['_id'])),
        'url': siteDoc['url'],
        'title': siteDoc['title'],
        'status': siteDoc['status'],
        'crawled': siteDoc['crawled']
    }

@blueprint.route('<string:id>')
@blueprint.route('', defaults={'id': 0})
def get(id):
    db = get_db()
    siteDoc = db['sites'].find_one({"_id": ObjectId(id)})
    site = normalize(siteDoc)
    return dumps(site)

@blueprint.route('/')
def get_list():
    db = get_db()
    sites = []
    for doc in db['sites'].find({}).sort([{'crawled', pymongo.DESCENDING}]):
        sites.append(normalize(doc))

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
