
#configuracion con la base de datos en mysql

class Config:
    SECRET_KEY = 'tu_secreto'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@127.0.0.1/db_julian2'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
