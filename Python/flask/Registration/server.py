from flask import Flask, render_template, redirect, request, session, flash
import re 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
app.secret_key = "some_super_secret"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/information', methods=['POST'])
def information():
    error = False

    if len(request.form['email']) < 1:
        flash("Email cannot be blank")
        error = True
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address")
        error = True

    if len(request.form['first_name']) < 1:
        flash("First Name cannot be blanl")
        error = True
    elif request.form['first_name'].isalpha:
        error = False
    else:
        flash("Please only use letters")
        error = True

    if len(request.form['last_name']) < 1:
        flash("First Name cannot be blanl")
        error = True
    elif request.form['last_name'].isalpha:
        error = False
    else:
        flash("Please only use letters")
        error = True

    if len(request.form['password']) < 8:
        flash("Password must contain more than 8 charachters")
        error = True

    if request.form['confirm'] != request.form['password']:
        flash("Password and Password Confirmation should match")
        error = True

    if error == True:
        return redirect('/')
    else:
        flash('Success')
        return redirect('/')

app.run(debug=True)

