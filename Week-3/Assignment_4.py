from flask import Flask, render_template, redirect, url_for,make_response
from flask import request

app = Flask(__name__)

@app.route('/trackName',methods=["POST"]) #步驟二：從表單取得 INPUT
def save():
    user_name = request.form["user_nm"]
    return redirect(url_for('trace',name=user_name))  #傳入 trace() 之參數 user_name



@app.route('/trackName',methods=["GET"])
def trace(name="name"): #query str(? 後字串) 為 "name"
    url_get = request.args.get('name') #步驟三：從 url 取得目標字串 get '?name=' 後面值

    resp = make_response(redirect(url_for("name"))) #建立空 response，request是全局request對象 #request是全局request對象 # 回到 name() 
    resp.set_cookie('userID', url_get) #設定 cookies

    return resp

 
@app.route('/myName') #步驟一：開始畫面
def name():
    if request.cookies.get('userID') is None: # cookies 已存 userID
        return render_template("name.html")
    else:                             # 無 userID
        return ' Done.'

app.run(debug=True, port=3000,host="0.0.0.0")