from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/history', methods =['GET'])
def get_history():
    return [] #get chat-history will be used on frontend and not for the api request

