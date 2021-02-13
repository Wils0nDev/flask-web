import os
import pymysql



pymysql.install_as_MySQLdb()

SECRET_KEY = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
PWD = os.path.abspath(os.curdir)	

DEBUG = True
SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(user='root', password='wilson1890', server='localhost', database='gestor_tareas')
SQLALCHEMY_TRACK_MODIFICATIONS = False