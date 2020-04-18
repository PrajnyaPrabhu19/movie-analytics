import os
from Modules import ParseDataset
from Modules import SearchFeatures

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
    search_inequality = request.args.get('search_inequality')

    responseObject = SearchFeatures.fetchMoviesByNumericSearch(search_field,search_query, search_inequality, moviesData)
    return jsonify(responseObject)

@app.route('/searchText', methods=['GET'])
def searchText():

    #Get all the parameters from the URL string
    search_field = request.args.get('search_field')
    search_query = request.args.get('search_query')

    responseObject = SearchFeatures.fetchMoviesByTextSearch(search_field, search_query, moviesData)
    return jsonify(responseObject)

@app.route('/searchFlopMovies', methods=['GET'])
def FlopMovies():
    # Get all the parameters from the URL string
    search_year = request.args.get('search_year')
    responseObject = SearchFeatures.searchFlopMovies(search_year, moviesData)
    return jsonify(responseObject)

@app.route('/highestGrossingMovie', methods=['GET'])
def grossMovie():
    # Get all the parameters from the URL string
    search_year = request.args.get('search_year')
    responseObject = SearchFeatures.highestGrossingMovie(search_year, moviesData)
    return jsonify(responseObject)


if __name__ == '__main__':
    app.run()
