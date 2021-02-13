from app import app
from flask import render_template
from flask import request
from models.esquema import *
import logging


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/register/',methods=['GET'])
@app.route('/register')
def register():
    logging.info('WISLON')
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


