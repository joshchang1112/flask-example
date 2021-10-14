from flask import Flask, Response
from flask_cors import CORS
import json
import logging
import pymysql

conn = pymysql.connect(
    host='player-database.cdsowpyuckv0.us-east-1.rds.amazonaws.com',
    port=3306,
    user='admin',
    password='JoshChang1112',
    db='player'
)

def get_details(table, column, value):
    cur = conn.cursor()
    value = ' '.join(value.split('_'))
    command = 'SELECT * FROM {} Where {} = {};'.format(
        table, table+'.'+column, '"' + value + '"'
    )
    print(command)
    cur.execute(command)
    details = cur.fetchall()
    return details

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
logger.setLevel(logging.INFO)

application = Flask(__name__)
CORS(application)


@application.route('/')
def hello_world():
    return '<h2>Welcome to player search website!</h2>'


@application.route('/teams/<teamname>')
def get_players_by_team(teamname):
    res = get_details('Profile', 'team_name', teamname)
    rsp = Response(json.dumps(res), status=200, content_type="application/json")
    return rsp


@application.route('/pos/<position>')
def get_players_by_position(position):
    res = get_details('Profile', 'first_position', position)
    rsp = Response(json.dumps(res), status=200, content_type="application/json")
    return rsp


if __name__ == '__main__':
    application.run(debug=True)
