from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)	

from controllers.usuario import *

#@app.errorhandler(404)
#def page_not_found(error):
#	return render_template("error.html",error="Página no encontrada..."), 404

if __name__ == '__main__':
    app.run(port=3000 , debug=True)



