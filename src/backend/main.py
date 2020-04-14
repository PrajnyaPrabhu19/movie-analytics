import os
from Modules import ParseDataset

from flask import Flask
from flask import request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

filePath = os.path.abspath(os.path.dirname(os.path.abspath(__file__))) + "/Data/tmdb_movies.csv"
moviesData = ParseDataset.parseCSV(filePath)

@app.route('/testConnection', methods=['GET'])
def getData():

    print(request.headers)
    return 'Hello Message!'


if __name__ == '__main__':
    app.run()