# This API test is based off of the flask API tutorial located at:
# https://www.codementor.io/sagaragarwal94/building-a-basic-restful-api-in-python-58k02xsiq
# and
# https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
#
# This will be the basic, barebones API as descried on this site

from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask import jsonify
from EmployeeHandler import EmployeeHandler

db_connect = create_engine('sqlite:///chinook.db')
app = Flask(__name__)
api = Api(app)

@app.route('/employees', methods=['GET'])
def get_employees():
    conn = db_connect.connect()
    query = conn.execute("select EmployeeId, LastName, FirstName from employees")
    result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
    return jsonify(result)

@app.route('/tracks', methods=['GET'])
def get_tracks():
    """Get all track information"""
    conn = db_connect.connect()
    query = conn.execute('select trackid, name, composer, unitprice from tracks;')
    result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
    return jsonify(result)

@app.route('/employees/<employee_id>', methods=['GET', 'POST'])
def employee_id(employee_id):
    if request.method == 'GET':
        """Get the informaiton for the <employee_id>"""
        conn = db_connect.connect()
        query = conn.execute('select * from employees where EmployeeID = %d;' % int(employee_id))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)
    if request.method == 'POST':
        """Modify/Update the informaiton for <employee_id>"""

        # Make a dictionary of received params
        receivedArgs = {}
        for sentArgs in request.args:
            receivedArgs[sentArgs] = request.args.get(sentArgs)

        # Send the dictionary to the employee handler and then return the status to the
        # API caller.
        statusDict = EmployeeHandler(employee_id, receivedArgs)

        print(statusDict)

        for key in statusDict:
            if key == 1:
                return "Failed - %s " % (statusDict[key])
            else:
                return "Pass"

    # If something goes wrong - the default it to fail
    return "Failed - Reached end of method without any actions"


@app.route('/genres', methods=['GET'])
def get_genres():
    conn = db_connect.connect()
    query = conn.execute('select * from genres')
    result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
    return jsonify(result)

if __name__ == '__main__':
    app.run(port='5002')