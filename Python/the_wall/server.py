# from flask import Flask, request, redirect, render_template, session, flash
# from datetime import datetime
# # import the Connector function
# from mysqlconnection import MySQLConnector
# from flask_bcrypt import Bcrypt
# import re 
# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

# app = Flask(__name__)
# bcrypt = Bcrypt(app) 
# app.secret_key = 'secrect_stu_ff'
# mysql = MySQLConnector(app, 'thewall') 

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/register', methods=['POST'])
# def register():

#     first_name = request.form['first_name']
#     last_name = request.form['last_name']
#     email = request.form['email']
#     password = request.form['password']
#     errors = False

#     if len(first_name) < 2:
#         flash('First name must be longer than 2 characters')
#         errors = True
    
#     if len(last_name) < 2:
#         flash('Last name must contain more than 2 characters')
#         errors = True

#     if not EMAIL_REGEX.match(email):
#         flash('Invalid email format. Please try again')
#         errors = True

#     if len(password) < 8:
#         flash('Password must contain 8 or more characters')
#         errors = True
    
#     if request.form['password_confrim'] != password:
#         flash('Password must be equal to Confirmation Password')
#         errors = True

#     if errors == True:
#         return redirect('/')

#     else:
#         #pull the user data from the database to register the email or check if it exists
#         user_query = "SELECT * FROM walldb.users WHERE email = :email LIMIT 1"
#         user_data = { 'email' :email }
#         user = mysql.query_db(user_query, user_data)

#         if len(user) > 0:
#             flash('Email address already exists, please login')
#             return redirect('/')
#         else:
#             #registration is validwe have to encrypt the password
#             password = bcrypt.generate_password_hash(password)
#             #now we push their info to db
#             insert_query = "INSERT INTO walldb.user (first_name, last_name, email, password, created_at) VALUE(:first_name, :last_name, :email, :password, NOW())"
#             insert_data = { 'first_name': first_name, 
#                             'last_name': last_name,
#                             'email': email,
#                             'password': password
#                         }
#             user = mysql.query_db(insert_query, insert_data)
#             print user #making sure that the increment goes up
#             session['x'] = user[0]['id']
#             return render_template('wall.html', first_name=first_name)



# @app.route('/login', methods=['POST'])
# def login():

#         first_name = request.form['first_name']
#         last_name = request.form['last_name']
#         login_email = request.form['login_email']
#         login_password = request.form['login_password']

#         login_query = "SELECT * FROM users WHERE email = :login_email LIMIT 1"
#         login_data = { 'email': login_email}
#         login_id = mysql.query_db(login_query, login_data)

#         if len(login_id) > 0:
#             pw_query = "SELECT password FROM users WHERE password = :password"
#             pw_data = { 'password': password }
#             pw = mysql.query_db(pw_query, pw_data)
#             if login_passwrod != password: 
#                 flash('Email or Password is incorrect')
#                 return redirect('/')
            
#             else:
#                 return render_template('wall.html', last_name=last_name)
        
#         else:
#             flash('Email or Password is incorrect. Please try again.')
#             return redirect('/')
# app.run(debug=True)



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
mysql = MySQLConnector(app, 'thewall')

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
        
    if len(password) < 8:
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
            pw= bcrypt.generate_password_hash(password)
            #now we will save their info to our users table
            insert_query = "INSERT INTO users (first_name, last_name, email, pw, created_at) VALUE(:first_name, :last_name, :email, :pw, NOW())"
            data = { 'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'pw':pw,
                }
            query = "SELECT * FROM users WHERE email= :email AND first_name=:first_name AND last_name= :last_name"
            user= mysql.query_db(query,data)
            session[ 'user' ] = user
            return redirect('/wall')
        return redirect('/')

    @app.route('/login', methods=['POST'])
    def login():

        first_name = request.form['first_name']
        last_name = request.form['last_name']
        login_email = request.form['login_email']
        login_password = request.form['login_password']
        
        if login_email and login_password:
            #Makes sure email and password were actually input
            query = "SELECT * FROM users WHERE email=:login_email"
            data = {
                'email': login_email
            }
            login_id = mysql.query_db(query, data)
            #checks if user matches in db
            if len(login_id) > 0:
                user = login_id[0]
                print("user: {}".format(user))
                if bcrypt.check_password_hash(user['pw'], pw):
                    #adding user to session
                    session['user'] = user
                    flash('Logged in Successfully')
                    return redirect('/wall')
            flash("Inccorect username or password")
            return redirect('/')
    
    @app.route('/wall')
    def wall():
        print (session['user'])
        if 'user' in session:
            query = "SELECT first_name, last_name, message_text, DATE_FORMAT(messages.created_at, '%M %D %Y %H:%i') AS messages.id, user_id FROM messages JOIN users ON messages.user_id = users.id ORDER BY messages.created_at DESC"
            message_list = mysql.query_db(query)
            #pirnts message list
            query = "SELECT first_name, last_name, comment_text, DATE_FORMAT(comments.created_at, '%M %D %Y %H:%i') AS created_at, message_id FROM comments JOIN users ON comments.user_id = user.id ORDER BY comments.created_at DESC"
            comment_list = mysql.query_db(query)
            #prints comment list
            return render_template('/wall.html', message_list=message_list, comment_list=comment_list)
        else:
            flash("You are not logged in")
            return redirect('/')

    @app.route('/wall/message', methods=["POST"])
    def add_message():
        message_text = request.form['message']
        query = "INSERT INTO messages (message_text, created_at, updated_at, user_id) VALUES (:message_text, NOW(), NOW(), :user_id)"
        data= {
            'message_text' :message_text, 
            'user_id': session['user']['id']
        }
        mysql.query_db(query, data) 
        return redirect('/wall')

    @app.route('/wall/comment/<message_id>', methods=["POST"])
    def add_comment(message_id):
        query = "INSERT INTO comments (comment_text, created_at, updated_at, user_id, message_id) VALUES (:comment_text, NOW(), NOW(), :user_id, :message_id)"
        data = {
            'comment_text' : request.form['comment'],
            'user_id' : session['user']['id'], 
            'message_id' : message_id
        }
        mysql.query_db(query, data) 
        return redirect('/wall')
app.run(debug=True)