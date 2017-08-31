from flask import Flask, request, redirect, render_template, session, flash
from datetime import datetime
# import the Connector function
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

app = Flask(__name__)
bcrypt = Bcrypt(app) 
app.secret_key = 'secretsauce'
mysql = MySQLConnector(app, 'logindb')

@app.route('/')
def index():

    return render_template('index.html') 

@app.route('/register', methods=['POST'])
def register():
    
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    errors = False

    if len(first_name) < 2:
        flash("First name must be more than 2 charachters")
        errors = True
       
    if len(last_name) < 2:
        flash('Last name must be more than 2 charachters')
        errors = True
        
    if not EMAIL_REGEX.match(email):
        flash('Invalid email format. Please try again')
        errors = True
        
    if len(password) <= 8:
        flash('Password must contain 8 or more charachters')
        errors = True
       
    if request.form['password_confirm'] != password:
        flash('Password must equal Confirmation Password')
        errors = True
        
    if errors == True:
        return redirect('/')

    else:
        user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
        user_data = { 'email': email }
        user = mysql.query_db(user_query, user_data)
        
        if len(user) > 0: #we have that email already
            flash('User already exists')
            return redirect('/')
        else:
            #after valid registration we can now bcrypt their password
            password = bcrypt.generate_password_hash(password)
            #now we will save their info to our users table
            insert_query = "INSERT INTO users (first_name, last_name, email, password, created_at) VALUE(:first_name, :last_name, :email, :password, NOW())"
            data = { 'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'password':password,
                }
            user_id = mysql.query_db(insert_query,data) 
            print user_id
            session[ 'user_id' ] = user_id
            return render_template('success.html', first_name=first_name)

    @app.route('/login', methods=['POST'])
    def login():

        first_name = request.form['first_name']
        last_name = request.form['last_name']
        login_email = request.form['login_email']
        login_password = request.form['login_password']
        

        login_query = "SELECT * FROM users WHERE email = :login_email LIMIT 1"
        login_data = { 'email': login_email}
        login_id = mysql.query_db(login_query, login_data)

        if len(login_id) > 0:
            pw_query = "SELECT password FROM users WHERE password = :password"
            pw_data = { 'password': password }
            pw = mysql.query_db(pw_query, pw_data)
            if login_passwrod != password: 
                flash('Email or Password is incorrect')
                return redirect('/')
                
                
            else:
                return render_template('success.html', last_name=last_name)
        else:
            flash('Email or Password is incorrect')
            return redirect('/')



app.run(debug=True)