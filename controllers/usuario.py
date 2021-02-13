from app import app,login_manager
from flask import render_template, url_for, redirect
from flask import request
from models.esquema import *
import flask_login


@app.route('/',methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        user = User.query.filter_by(email=request.form['email']).first()
        print(user)
        if user and user.verify_password(request.form['password']):
            flask_login.login_user(user)

            next_page = url_for('proyect')
            return redirect(next_page)
            
        else:
            print("Login ivalido!")
    else:
        print('error')

    return render_template('login.html')


@app.route('/register/',methods=['GET'])
@app.route('/register')
def register():

    return render_template('user/register.html')

@app.route('/adduser',methods=['POST'])
def adduser():
    if request.method == 'POST':
        admin = User(
            name=request.form['name'], 
            surname=request.form['surname'],
            email=request.form['email'],
            password=request.form['password']
            )
        db.session.add(admin)
        db.session.commit()

    return render_template('user/register.html')

@app.route("/proyect",methods=['GET'])
@flask_login.login_required
def proyect():
    return render_template('app/proyecto.html')

@app.route('/logout')
def logout():
    flask_login.logout_user()
    return redirect(url_for('index'))

