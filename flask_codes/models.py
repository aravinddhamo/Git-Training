from flask_codes import db
from datetime import datetime

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    ClientId=db.Column(db.String(20),unique=True,nullable=True)
    ClientName=db.Column(db.String(120),unique=True,nullable=True)
    ClientType=db.Column(db.String(20),nullable=True)
    ClientBSI=db.Column(db.String(20),nullable=True)
    ClientStatus=db.Column(db.String(20),nullable=True)
    date_created=db.Column(db.DateTime,default=datetime.utcnow)

def __repr__(self):
    return f'{self.ClientId} : {self.ClientName} : {self.date_created}'