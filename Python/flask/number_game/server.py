from flask import Flask, render_template, redirect, request, session
import random
app = Flask(__name__)
app.secret_key = "secret"

@app.route('/')
def index():
    if 'randnum' not in session:
       session['randnum'] = random.randint(1,101)
       

    return render_template('index.html')

@app.route('/play', methods=['POST'])
def gamePlay():
    if int(request.form['guess'])  > session['randnum']:
        session['message'] = "Too High, guess again"
    elif int(request.form['guess']) < session['randnum']:
        session['message'] = "Too Low, guess again"
    else:
        session['message'] = "Perfect Guess!"

  
    return redirect('/')

@app.route('/reset', methods = ['POST'])
def reset():
    # session.pop(request.form['guess'])
    session.pop('message')
    return redirect('/')



app.run(debug=True)