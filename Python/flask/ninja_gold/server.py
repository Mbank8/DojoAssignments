from flask import Flask, render_template, redirect, request, session
import random, datetime
app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route('/')
def index():
    if "my_gold" not in session:
        session['my_gold'] = 0
        session["activities"] = [ ]
    print session #TDD to see my current gold number
    return render_template('index.html')

@app.route('/process_money', methods = ['POST'])
def money():

    date=datetime.datetime.now().strftime("%Y/%m/%d %X %p")

    if request.form["building"] == "Farm":
        gold = random.randint(10,20)
        session["my_gold"] += gold
        session["activities"].append(("You earned", gold, "gold from the farm! (", date, ")"))

    elif request.form["building"] == "Cave":
        gold = random.randint(5,10)
        session["my_gold"] += gold
        session["activities"].append(("You earned", gold, "gold from the cave! (",date, ")"))
    
    elif request.form["building"] == "House":
        gold = random.randint(2,5)
        session["my_gold"] += gold
        session["activities"].append(("You earned",gold,"gold from the house! (", date, ")"))

    else:
        gold = random.randint(-50,51)
        session["my_gold"] += gold
        if gold > 0:
            session["activities"].append(("You entered the casino and won",gold,"gold!... Nice! (", date, ")"))
        else:
            session["activities"].append(("You entered the casino and lost", gold, "gold...Ouch.. (", date, ")"))

    return redirect('/')

@app.route("/refresh", methods=["POST"])
def winner():
    session.clear()
    return redirect('/')

app.run(debug=True)
            