from flask import Flask 
from flask import request
import re

app = Flask(__name__)


@app.route('/data',methods=["GET"])
def index2(name="number"):

    get_str = request.args.get('number',"Lack of Parameter")
    length = len(get_str) #用長度確認是否整個 str 為 int
    maybe_num = re.match(r'^\+?[1-9][0-9]*$',get_str) #檢查正整數，type 為 str

    if get_str == "Lack of Parameter": #localhost:3000/data
        return "Lack of Parameter"

                                        #localhost:3000/data?number=5
    elif maybe_num is not None: # 為正整數
        str_num = maybe_num.group(0) #取第一個
        if len(str_num ) == length: #全字串為正整數
            url_num = int(str_num)
            total =0
            for i in range(1,url_num+1):
                total = total + i
            return str(total)
    elif maybe_num is None: #localhost:3000/data?number=xyz
        return "Wrong Parameter"


app.run(debug=True, port=3000,host="0.0.0.0")
