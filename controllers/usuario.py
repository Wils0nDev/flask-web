from app import app,login_manager
from flask import render_template, url_for, redirect
from flask import request
from models.esquema import *
from utils.formvalidate import SignupForm

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


#ruta de registro
@app.route('/register/',methods=["GET","POST"])
def register():
    form = SignupForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        next = request.args.get('next', None)
        if next:
            return redirect(next)
        return redirect(url_for('index'))
    return render_template('user/register.html', form=form)


#Para agregar usuarios
@app.route('/adduser',methods=['GET'])
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



@app.route('/logout')
def logout():
    flask_login.logout_user()
    return redirect(url_for('index'))

