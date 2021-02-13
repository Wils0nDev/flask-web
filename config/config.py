import os
import pymysql



pymysql.install_as_MySQLdb()

ecret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
PWD = os.path.abspath(os.curdir)	

DEBUG = True
SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(user='root', password='wilson1890', server='localhost', database='gestor_tareas')
SQLALCHEMY_TRACK_MODIFICATIONS = False