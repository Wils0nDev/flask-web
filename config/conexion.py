import pymysql.cursors

class Connection:
    def __init__(self):

    @staticmethod
    def connect()
    connection = pymysql.connect(host='localhost',
                             user='',
                             password='',
                             database='gestor_tareas',
                             cursorclass=pymysql.cursors.DictCursor)
    return connection