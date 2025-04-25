# app.py
from flask import Flask, request, jsonify, render_template
import openai
import os

app = Flask(__name__)

# Load your API key
openai.api_key = "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"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a dietician chatbot. Ask questions to learn user info and give personalized diet advice."},
            {"role": "user", "content": user_message}
        ]
    )
    reply = response['choices'][0]['message']['content']
    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(debug=True)

