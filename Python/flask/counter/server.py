from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "secret"

@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 0

    return render_template('index.html')

@app.route('/submit')
def submit():
    session['counter'] +=1
    return render_template('/submit.html')
    return redirect('/submit', counter=session['counter'])
    

app.run(debug=True)