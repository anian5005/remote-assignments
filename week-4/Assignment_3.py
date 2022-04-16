from flask import Flask, render_template, redirect, url_for,request,flash
import pymysql
from use_sql import check, add
 

app = Flask(__name__)
app.secret_key = "Your Key" #for flash message

@app.route('/home')
def index():

    return render_template("home.html")


@app.route('/login' , methods=["POST","GET"])
def login():
    email = request.form["email"] #user input data from sign-in form
    password = request.form["password"]
    result = check.check_user(email,password) #check model:search email from sql database and check the password is correct

    if result == "ISmember": #sign-in successfully
        flash("Sign-in Successfully.")
        return redirect(url_for('member'))

    elif result == "wrong_password": #sign-in failed
        flash('wrong password. please check and try again.')
        return redirect(url_for('index'))
        #return render_template("home.html")

    elif result == None: #sign-in failed
        flash('The email you entered does not exist. Please check that you have typed correctly.')
        return redirect(url_for('index'))
    else:
        flash('try again')
        return redirect(url_for('index'))

@app.route('/signup' ,methods=["POST","GET"])
def signup():
    email = request.form["email"] #user input data from sign-up form
    password = request.form["password"]
    check_result = check.check_user(email,password)
    
    if check_result == "ISmember":
        flash('Account already exists, please sign in!')
        return redirect(url_for('index'))
    
    else:
        add_result = add.add_user(email,password) #add model: if new email then add it to database


        if add_result == "Added":
            flash("Sign-up Successfully.")
            return redirect(url_for('member'))

        else:
            flash('Sign-up Failed,plaease try again!')
            return render_template("home.html")


@app.route('/member' )
def member():
    flash('Welcome!')
    return render_template("member.html")

app.run(debug=True, port=3000,host="0.0.0.0")