from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = "ShhItsASecret"
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['Post'])
def process():
    if len(request.form['name']) < 1 or request.form['name'] == 'Jake':
        flash("DENIED! You fucking suck, bud")
    else:
        flash("WooHoo You did it! {}".format(request.form['name']))
    return redirect('/')

app.run(debug=True)