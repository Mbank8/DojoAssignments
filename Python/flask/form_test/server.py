from flask import Flask, render_template, request, redirect, session 
app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route('/')
#the index handles rendering the form
def index():
    return render_template("index.html")
#the post will handle the form submission
@app.route('/users', methods=['POST'])
def create_user():
    print "Got Post Info"
    session['name'] = request.form['name']
    session['email'] = request.form['email']
    #below we will redirect back to index after submit
    return redirect('/show')
@app.route('/show')
def show_user():
    return render_template("user.html", name=session['name'], email=session['email')
app.run(debug=True)

