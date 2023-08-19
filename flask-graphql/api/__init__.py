from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/gql/v1')
def hello():
    return 'My First API !!'