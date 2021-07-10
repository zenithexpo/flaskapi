import flask
from flask import request, jsonify
import csv

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return 

data = [ ]

def read_csv():
	with open('test.csv') as f:
    data = [{k: int(v) for k, v in row.items()}
        for row in csv.DictReader(f, skipinitialspace=True)]


@app.route('/courses', methods=['GET'])
def api_id():

    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    results = []

    for student in data:
        if data['id'] == id:
            results.append(student)

    return jsonify(results)

@app.route('/learning_routine', methods=[''])

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

app.run()