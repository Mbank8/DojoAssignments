from flask import Flask, request, redirect, render_template, session, flash
from datetime import datetime
# import the Connector function
from mysqlconnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')


app = Flask(__name__)
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, "emailvalid")
app.secret_key = 'Thisisnotnotasecret'

@app.route('/')
def index():
    #insert mysql stuff
    # query = "SELECT * FROM users"
    # users = mysql.query_db(query)
    # print users
    return render_template('index.html')
def create(request):
    query = ":INSERT INTO users (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"
    data = {
        'email': request.form['email']
            }
    mysql.query_db(query, data) 

def display():
    query = "SELECT * FROM users"
    emails = mysql.query_db(query)
    return render_template("success.html", users=emails)


@app.route('/create',methods=['POST'])
def success():
    passFlag = True
    if len(request.form['email']) < 1:
        flash('Error! Invalid email', 'wrong')
        passFlag = False
        return render_template('success.html')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash ('Invalid email format. Please try again.', 'wrong')
        passFlag = False
        return render_template('success.html')
    if passFlag == True:
        flash ('The email address you entered is a valid email address. Thank you!', 'success')
        return display()

@app.route('/reset', methods=['POST'])
def reset():
    return redirect('/')


app.run(debug=True)