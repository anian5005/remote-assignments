from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def index():
    return render_template("index.html")



@app.route('/product')
def getproduct():
    return render_template("product.html")

app.run(debug=True, port=3000,host="0.0.0.0")