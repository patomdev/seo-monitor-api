import pymongo
import os
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
    """
    Returns one page
    ---
    description: Returns site by ID
    summary: Find site by ID
    operationId: get
    produces:
    - application/json
    - text/html
    tags:
      - sites
    parameters:
      - name: id
        in: path
        description: Id of site to use
        required: true
        type: string
    responses:
      200:
        description: Returns one page
    """
    db = get_db()
    siteDoc = db['sites'].find_one({"_id": ObjectId(id)})
    site = normalize(siteDoc)
    return dumps(site)

@blueprint.route('')
def get_list():
    """
    Get all sites
    ---
    description: Returns list of sites
    summary: Returns a list of sites
    tags:
      - sites
    responses:
      200:
        description: Returns a list of sites
    """
    db = get_db()
    sites = []
    for doc in db['sites'].find({}).sort([{'crawled', pymongo.DESCENDING}]):
        sites.append(normalize(doc))

    return dumps(sites)

@blueprint.route('', methods=['POST'])
@flaskparser.use_kwargs(FILTER)
def post(url, title):
    """
    Creates new site
    ---
    summary: Creates new site
    tags:
      - sites
    definitions:
      - schema:
          id: Site
          properties:
            id:
             type: string
             description: the site's name
    parameters:
      - in: body
        name: body
        schema:
          required:
            - url
            - title
          properties:
            url:
              type: string
              description: crawled url
            title:
              type: string
              description: title of page
    responses:
      201:
        description: Data of site

    """
    db = get_db()
    db['sites'].insert_one({'url': url, 'title': title})

    return jsonify({'status': 'ok'}), 201

@blueprint.route('<int:id>', methods=['PUT'])
@flaskparser.use_kwargs(FILTER)
def put(id, url, title):
    """
    Updates site
    ---
    summary: Updates site
    tags:
      - sites
    definitions:
      - schema:
          id: Site
          properties:
            id:
             type: string
             description: the site's name
    parameters:
      - in: body
        name: body
        schema:
          id: Site
          required:
            - url
            - title
          properties:
            url:
              type: string
              description: crawled url
            title:
              type: string
              description: title of page
    responses:
      200:
        description: Updated data of site

    """
    return jsonify({'id': id, 'url': url, 'title': title})

