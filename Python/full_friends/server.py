from flask import Flask, request, redirect, render_template, session, flash
from datetime import datetime
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'full_friends')

@app.route('/')
def index():
    query = "SELECT * FROM users"
    users = mysql.query_db(query)
    return render_template('index.html', all_users = users)


@app.route('/friends', methods=['POST'])
def create():
    query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW())"
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email']
            }
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/friends/<id>/edit', methods=["POST"])
def edit(id):
    query = "Select * FROM users WHERE id = :specific_id"
    data = {
            "specific_id": id
            }
    users = mysql.query_db(query, data) 
    return render_template("edit.html", edit_user=users[0])


@app.route('/friends/<id>', methods=['POST'])
def update(id):
    query = "UPDATE users SET first_name = :first_name, last_name= :last_name, email= :email, updated_at=NOW() WHERE id = :id"
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        'id':id
            }
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/friends/<id>/delete', methods=["POST"])
def destroy(id):
    query = "DELETE FROM users WHERE id = :id"
    data = {'id': id}
    mysql.query_db(query, data)
    return redirect('/')


app.run(debug=True)