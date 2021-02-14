from app import app,login_manager
from flask import render_template, url_for, redirect
from flask import request
from models.esquema import *
import flask_login

@app.route("/proyect/",methods=['GET'])
@flask_login.login_required
def proyect():
    page = request.args.get('page','')
    if page.isnumeric() : 
        print(len(page))
    else:
        print('no es numero')
    return render_template('app/proyecto.html')
