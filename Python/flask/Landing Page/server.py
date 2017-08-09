from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')

def index():
    return render_template("index.html")

@app.route('/ninja')

def ninja():
    return render_template("ninja.html")


@app.route('/dojos')

def dojos():
    return render_template("dojos.html")

@app.route('/new', methods=['POST'])
def new_user():
    print "Got post info"
    name = request.form['name']
    email = request.form['email']
    return redirect('/')

app.run(debug=True)