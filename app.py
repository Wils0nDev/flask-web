from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from config import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)	

login_manager = LoginManager()
login_manager.init_app(app)

from controllers.usuario import *

#@app.errorhandler(404)
#def page_not_found(error):
#	return render_template("error.html",error="Página no encontrada..."), 404

if __name__ == '__main__':
    app.run(port=3000 , debug=True)



