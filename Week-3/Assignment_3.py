from flask import Flask, render_template, redirect, url_for
from flask import request
#from flask.globals import request
#from requests import request
import re

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, My Server!"

@app.route('/data',methods=["GET"])
def index2(name="number"):

    get_str = request.args.get('number',"Lack of Parameter")
    length = len(get_str) 
    maybe_num = re.match(r'^\+?[1-9][0-9]*$',get_str)

    if get_str == "Lack of Parameter":
        return "Lack of Parameter"

                                        
    elif maybe_num is not None: 
        str_num = maybe_num.group(0)
        if len(str_num ) == length:
            url_num = int(str_num)
            total =0
            for i in range(1,url_num+1):
                total = total + i
            return str(total)
    elif maybe_num is None:
        return "Wrong Parameter"

@app.route('/sum.html')
def sum():

    return render_template("sum.html")


@app.route('/save',methods=["POST"])
def save():
     input_num = request.form['num_save']
     return redirect(url_for('sum'))


app.run(debug=True, port=3000,host="0.0.0.0")
