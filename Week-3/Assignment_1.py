from flask import Flask 

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, My Server!"

app.run(debug=True, port=3000,host="0.0.0.0")