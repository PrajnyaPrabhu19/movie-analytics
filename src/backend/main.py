import os
from Modules import ParseDataset

from flask import Flask
from flask import request
from flask_cors import CORS
from flask import jsonify

import json

app = Flask(__name__)
CORS(app)

filePath = os.path.abspath(os.path.dirname(os.path.abspath(__file__))) + "/Data/tmdb_movies.csv"
moviesData = ParseDataset.parseCSV(filePath)

@app.route('/testConnection', methods=['GET'])
def getData():

    print(request.headers)
    return 'Hello Message!'

@app.route('/searchNumeric', methods=['GET']) 
def search():

    #Get all the parameters from the URL string
    search_field = request.args.get('search_field')
    search_query = request.args.get('search_query')

    #Code for operations
    operations = {
    '0' : '=',
    '1' : '>',
    '2' : '>=',
    '3' : '<',
    '4' : '<='
    }
    search_inequality = request.args.get('search_inequality')

    responseObject = []

    for movie in moviesData:
        try:
            if (eval(movie[search_field]+operations[search_inequality]+search_query)):
                responseObject.append(movie)

        except Exception as e:
            print(e)

    return jsonify(responseObject)



if __name__ == '__main__':
    app.run()