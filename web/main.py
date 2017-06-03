import numpy as np
from flask import Flask, abort, jsonify, request, render_template
import cPickle as pickle
import os.path as path

output_file = path.join(path.dirname(__file__), '../rfc.pkl')
rfc = pickle.load(open(output_file, "rb"))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api', methods=['POST'])
def make_predict():
    # TODO: error cheching

    # convert to 2d array
    data = request.get_json(force=True)

    # for test
    # request_data = [[ data['county'], data['sex'] ]]
    # return jsonify(results = request_data)

    testSet = []
    for i in range(1, 42):
        row = [ data['county'], data['sex'] ] + [i]
        testSet.append(row)

    # result
    y_hat = rfc.predict(testSet)
    return jsonify(y_hat.tolist()) # can't return numpy array

if __name__ == '__main__':
    app.run(port = 5000, debug = True)