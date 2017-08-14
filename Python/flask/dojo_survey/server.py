from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = "Thisisabigsecret"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['post'])
def results():
    errors = False

    if len(request.form['name']) < 1:
        flash("Please enter valid name")
        errors = True

    if len(request.form['location']) < 1:
        flash("Please enter valid location")
        errors = True

    if len(request.form['language']) < 1:
        flash("Please enter valid language")
        errors = True

    if len(request.form['comment']) > 120:
        flash("Please keep comments between 1 and 120 characters")
        errors = True
    
    if errors == True:
        return redirect('/')
    else:
        return render_template('result.html', user = request.form)
    
app.run(debug=True)