
from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'i<3secrets'

from mysqlconnection import MySQLConnector
mysql = MySQLConnector (app, 'full_friends')


@app.route('/')
def index():
    flash('Here are all your friends!')
    query = 'SELECT id, First_name, last_name, email, created_at from full_friends.users';
    users = mysql.query_db(query)
    return render_template('index.html', users=users)

@app.route('/', methods =['POST'])
def create():
    print request.form['email']
    query = 'INSERT INTO users(First_name,last_name, email, created_at) values(:First_name, :last_name, :email, now())'
    data = {
    'First_name': request.form["first_name"],
    'last_name' : request.form["last_name"],
    'email': request.form["email"],
    }
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/friends/<id>/edit',methods =['get'] )
def edit(id):
    return render_template('edit.html', id = id)


@app.route('/friends/<id>', methods =['POST'])
def update(id):
    print id
    query= 'UPDATE users SET First_name= :First_name, last_name =:last_name,email = :email, created_at = now() WHERE id =' +id;
    data = {
    'First_name': request.form["first_name"],
    'last_name' : request.form["last_name"],
    'email': request.form["email"],
    }
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/friends/<id>/delete', methods =['POST'])
def delete(id):
    # return render_templateeturn redirect('/')"edit.html", username=id)
     query = 'DELETE from users WHERE id = ' +id   ;
     mysql.query_db(query)
     print query
     return redirect('/')


# @app.route('/email', methods = ['POST'])
# def checkemail():
#     print request.form['email']
#     if not EREG.match(request.form['email']):
#         flash('Email is not vaild!')
#         return redirect('/')
#     else:
#         query = 'insert into user_emails(email, created_at, updated_at) values(:email, now(), now())'
#         data = {
#         'email': request.form["email"]
#         }
#         mysql.query_db(query, data)
#
#         return redirect('/show')
#
#
# @app.route('/show')
# def show():
#     flash('The email address you entered is a VALID email address!')
#     query = 'SELECT * FROM emails.user_emails;'
#     users = mysql.query_db(query)
#     return render_template('success.html', users=users)

app.run(debug=True)
