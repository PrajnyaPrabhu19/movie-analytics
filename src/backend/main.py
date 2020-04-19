import os
from Modules import ParseDataset
from Modules import SearchFeatures

from flask import Flask
from flask import request
from flask_cors import CORS
from flask import jsonify

import json

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
CORS(app)

filePath = os.path.abspath(os.path.dirname(os.path.abspath(__file__))) + "/Data/tmdb_movies.csv"
moviesData = ParseDataset.parseCSV(filePath)

@app.route('/headers', methods=['GET'])
def getData():
    response = {
        'id': 'text',
        #'imdb_id': 'text',
        #'popularity': 'numeric',
        'budget': 'numeric',
        'revenue': 'numeric',
        'original_title': 'text',
        'cast': 'text',
        #'homepage': 'text',
        #'director': 'text',
        #'tagline': 'text',
        #'keywords': 'text',
        'runtime': 'numeric',
        #'genres': 'text',
        #'production_companies': 'text',
        #'release_date': 'text',
        #'vote_count': 'numeric',
        #'vote_average': 'numeric',
        #'release_year': 'numeric',
        #'budget_adj': 'numeric',
        #'revenue_adj': 'numeric'
    }
    return jsonify(response)

@app.route('/searchNumeric', methods=['GET']) 
def search():

    #Get all the parameters from the URL string
    search_field = request.args.get('search_field')
    search_query = request.args.get('search_query')
    search_inequality = request.args.get('search_inequality')

    responseObject = SearchFeatures.fetchMoviesByPopularity(search_field,search_query, search_inequality, moviesData)
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
