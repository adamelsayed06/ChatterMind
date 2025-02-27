from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/get-response', methods = ['POST']) #get response from openai, but passes in user input as a query
def get_response():
    return [] #api call to get_openai as well as user input 


@app.route('/history', methods =['GET'])
def get_history():
    return [] #get chat-history will be used on frontend and not for the api request

