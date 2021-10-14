from flask import Flask, Response
from flask_cors import CORS
import json
import logging

from application_services.imdb_artists_resource import IMDBArtistResource
from application_services.students_resource import StudentsResource
from application_services.UsersResource.user_service import UserResource
from database_services.RDBService import RDBService as RDBService

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
logger.setLevel(logging.INFO)

application = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return '<u>Hello World!</u>'


@app.route('/imdb/artists/<prefix>')
def get_artists_by_prefix(prefix):
    res = IMDBArtistResource.get_by_name_prefix(prefix)
    rsp = Response(json.dumps(res), status=200, content_type="application/json")
    return rsp


@app.route('/users/')
def get_total_users_info():
    res = UserResource.get_users_info()
    rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
    return rsp

@app.route('/users/<prefix>')
def get_users_name_prefix(prefix):
    res = StudentsResource.get_by_name_prefix(prefix)
    rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
    return rsp


@app.route('/<db_schema>/<table_name>/<column_name>/<prefix>')
def get_by_prefix(db_schema, table_name, column_name, prefix):
    res = RDBService.get_by_prefix(db_schema, table_name, column_name, prefix)
    rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
    return rsp


if __name__ == '__main__':
    application.run()
