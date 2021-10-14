from flask import Flask, Response, request
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

def get_details(table, column=None, value=None):
    cur = conn.cursor()
    if not column:
        command = 'SELECT * FROM {};'.format(table)
    else:
        value = ' '.join(value.split('_'))
        command = 'SELECT * FROM {} Where {} = {};'.format(
            table, table+'.'+column, '"' + value + '"'
        )
    cur.execute(command)
    details = cur.fetchall()
    return details

def get_positions(table, value):
    cur = conn.cursor()
    command = 'SELECT * FROM {} Where {} = {} or {} = {};'.format(
        table, table+'.first_position', '"' + value + '"', 
        table+'.second_position', '"' + value + '"'
    )
    cur.execute(command)
    details = cur.fetchall()
    return details

def insert_player(table):
    cur = conn.cursor()

    firstName = '"' + request.form.get('first_name') + '",'
    lastName = '"' + request.form.get('last_name') + '",'
    fullName = '"' + request.form.get('full_name') + '",'
    firstPosition = '"' + request.form.get('first_Position') + '",'
    secondPosition = '"' + request.form.get('second_Position') + '",'
    teamCity = '"' + request.form.get('team_city') + '",'
    teamName = '"' + request.form.get('team_name') + '",'
    teamLeague = '"' + request.form.get('team_league') + '",'
    teamDivision = '"' + request.form.get('team_division') + '",'
    number = request.form.get('number') + ','
    height = request.form.get('height') + ','
    weight = request.form.get('weight') + ','
    age = request.form.get('age')
    
    columns = "(first_name, last_name, full_name, first_Position, second_Position, team_city, team_name, \
        team_league, team_division, number, height, weight, age)"
    value = (firstName + lastName + fullName + firstPosition + secondPosition + 
        teamCity + teamName + teamLeague + teamDivision + number + height + weight + age)
    

    command = 'Insert Into {} {} Values ({})'.format(table, columns, value)
    cur.execute(command)
    conn.commit()
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


@application.route('/players')
def get_all_players():
    res = get_details('Profile')
    rsp = Response(json.dumps(res), status=200, content_type="application/json")
    return rsp

@application.route('/<column>/<value>')
def get_players_by_key_values(column, value):
    res = get_details('Profile', column, value)
    rsp = Response(json.dumps(res), status=200, content_type="application/json")
    return rsp

@application.route('/pos/<position>')
def get_players_by_position(position):
    res = get_positions('Profile', position)
    rsp = Response(json.dumps(res), status=200, content_type="application/json")
    return rsp

@application.route('/insert', methods = ['POST'])
def add_player():
    res = insert_player('Profile')
    rsp = Response(json.dumps(res), status=200, content_type="application/json")
    return rsp



if __name__ == '__main__':
    application.run(debug=True)
