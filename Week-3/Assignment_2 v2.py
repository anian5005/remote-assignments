from flask import Flask 
from flask import request

app = Flask(__name__)

@app.route('/data',methods=["GET"])
def index2(name="number"):

    get_str = request.args.get('number',"Lack of Parameter")
  

    if get_str == "Lack of Parameter": #localhost:3000/data
        return "Lack of Parameter"
 
    elif get_str.isdigit():
        total =0
        for i in range(1,int(get_str)+1): #localhost:3000/data?number=5
            total = total + i
        return str(total)
    else:
        return "Wrong Parameter"


app.run(debug=True, port=3000,host="0.0.0.0")
