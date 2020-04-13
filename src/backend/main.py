from flask import Flask
from flask import request
from flask_cors import CORS
import json
app = Flask(__name__)
CORS(app)


@app.route('/testConnection', methods=['GET'])
def getData():

    print(request.headers)
    return 'Hello Message!'


if __name__ == '__main__':
    app.run()