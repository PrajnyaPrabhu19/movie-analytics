import os
from Modules import ParseDataset
from Modules import SearchFeatures
from Modules import DatasetOperations
from Modules import AnalyticsFeatures
from Modules import ImportExport

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
    responseObject = AnalyticsFeatures.searchFlopMovies(search_year, moviesData)
    return jsonify(responseObject[-10:])

@app.route('/highestGrossingMovie', methods=['GET'])
def grossMovie():
    # Get all the parameters from the URL string
    search_year = request.args.get('search_year')
    responseObject = AnalyticsFeatures.highestGrossingMovie(search_year, moviesData)
    return jsonify(responseObject)

@app.route('/highestGrossingDirector', methods=['GET'])
def grossDirector():
    # Get all the parameters from the URL string
    search_year = request.args.get('search_year')
    responseObject = SearchFeatures.highestGrossingDirector(search_year, moviesData)
    return jsonify(responseObject)

@app.route('/highestGrossingActorYear', methods=['GET'])
def highestPaidActor():
    # Get all the parameters from the URL string
    search_year = request.args.get('search_year')
    responseObject = SearchFeatures.highestGrossingActorYear(search_year, moviesData)
    return jsonify(responseObject)

@app.route('/insertData', methods =['POST'])
def insertData():
    data = request.data
    final_data = eval(data)
    global moviesData
    moviesData = DatasetOperations.insertMovie(final_data, moviesData)
    return jsonify({'message':'success'})

@app.route('/editData', methods =['POST'])
def editData():
    data = request.data
    new_data = eval(data)
    global moviesData
    moviesData = DatasetOperations.updateMovie(new_data, moviesData)
    return jsonify({'message':'update successful'})

@app.route('/deleteMovie', methods = ['POST'])
def deleteData():
    data = request.data
    global moviesData
    moviesData = DatasetOperations.deleteMovie(eval(data), moviesData)
    return jsonify({'message':'deleted successfully'})

@app.route('/aggregateMoviesBR', methods =['GET'])
def aggregateMovies():
    responseObject = AnalyticsFeatures.moviesAggregate(moviesData)
    return jsonify(responseObject)

@app.route('/analyticsGrenre', methods =['GET'])
def analyticsGenre():
    search_year = request.args.get('search_year')
    responseObject = AnalyticsFeatures.analyticsGrenre(search_year, moviesData)
    return jsonify(responseObject)

@app.route('/importData', methods =['POST'])
def importData():
    data = request.data
    global moviesData
    moviesData = ImportExport.importData(eval(data))
    return jsonify({'Imported new data'})

if __name__ == '__main__':
    app.run()
