DB = 'mysql'
DRIVER = 'pymysql'
NAME = 'root'
PWD = 'root'
HOST = 'localhost'
PORT = 3306
DB_NAME = 'flask_program_1226'
CHARSET = 'utf8'

SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset={}'.format(DB, DRIVER, NAME, PWD, HOST, PORT, DB_NAME,
                                                                     CHARSET)