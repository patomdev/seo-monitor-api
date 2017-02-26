import pymongo
from flask import g
from flask import current_app as app

def get_db():
    if not hasattr(g, 'conn'):
        g.conn = pymongo.MongoClient(
            app.config['MONGODB_HOST'],
            int(app.config['MONGODB_PORT'])
        )

    if not hasattr(g, 'db'):
        g.db = g.conn[app.config['MONGODB_DB']]
    return g.db

# todo
# @app.teardown_appcontext
# def teardown_db(exception):
#     conn = getattr(g, 'conn', None)
#     if conn is not None:
#         conn.close()