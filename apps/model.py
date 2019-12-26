from flask_sqlalchemy import SQLAlchemy
from apps import app

db = SQLAlchemy(app=app)

class Goods(db.Model):
    __tablename__ = 't_goods'
    # 改字段类型是识别不了的，映射不到数据库
    id = db.Column(db.Integer,primary_key=True)
    gname = db.Column(db.String(80),unique=True)
    gtype = db.Column(db.String(2))
    price = db.Column(db.String(5))




