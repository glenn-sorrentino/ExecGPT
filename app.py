import os
import requests
from flask import Flask, render_template, request
from dotenv import load_dotenv

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

# Get the ChatGPT API key from the environment
API_KEY = os.getenv('CHATGPT_API_KEY')
API_URL = 'https://api.openai.com/v1/engines/text-davinci-002/completions'

headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}

@app.route("/", methods=["GET", "POST"])
def index():
    response_text = ""
    response = None
    
    if request.method == "POST":
        user_input = request.form["user_input"]
        data = {
            "prompt": user_input,
            "max_tokens": 50,
            "temperature": 0.8,
            "n": 1
        }

        response = requests.post(API_URL, json=data, headers=headers)
        if response.status_code == 200:
            response_text = response.json()["choices"][0]["text"].strip()
        else:
            response_text = f"Error {response.status_code}: {response.text}"

    return render_template("index.html", response_text=response_text)

if __name__ == "__main__":
    app.run(debug=True)
