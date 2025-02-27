from openai import OpenAI
from flask import Flask, jsonify, request #request used for query parameters for user input
from flask_cors import CORS

app=Flask(__name__)
CORS(app)
client = OpenAI()

@app.route('/get_openai', methods=['POST'])
def get_openai():
    data = request.json
    user_input = data.get('user_input') #json field named user input

    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
    {"role": "system", "content": "You are a life coach"},
        {
                "role": "user",
                "content": user_input
        }
    ])
    return jsonify(completion.choices[0].message)

