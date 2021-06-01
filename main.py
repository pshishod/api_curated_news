import flask
from flask import request, jsonify
import csv
app = flask.Flask(__name__)     # Allow the flask object to be created, so that we can call methods such as app.run()
app.config["DEBUG"] = True      # Allow debugging, to more easily debug the code if problems arise

# Create some test data for our catalog in the form of a list of dictionaries.
dataset = []        # Store the data in an araay called dataset
reader = csv.DictReader(open('./dataset.csv'))
for row in reader:
    dataset.append(row)


@app.route('/', methods=['GET'])    # Attach the location '/' with the function home()
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/books/all', methods=['GET'])  # Attach this location to the function api_all
def api_all():
    return jsonify(dataset)

# A route to return entries based on the keyword filtering.
@app.route('/api/v1/resources/books', methods=['GET'])
def api_keyword():
    if 'keyword' in request.args:
        keyword = str(request.args['keyword'])
        print(keyword)
    else:
        return "Error: no keyword specified. Please specify a keyword"

    results = []
    for i in dataset:
        if keyword.lower() in i['summary'].lower():
            results.append(i)
    return jsonify(results)

app.run()