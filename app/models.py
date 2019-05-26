from app import db, ma
from datetime import datetime


class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), unique=True)
  email = db.Column(db.String(120), unique=True)

  def __init__(self, username, email):
    self.username = username
    self.email = email

  def __repr__(self):
    return '<User %r>' %self.username

class Flight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    matricula_aluno = db.Column(db.String())
    date = db.Column(db.Date())
    dateTimeStart = db.Column(db.DateTime())
    dateTimeEnd = db.Column(db.DateTime())
    comment = db.Column(db.Text())

    def __init__(self, matricula_aluno, date, dateTimeStart, dateTimeEnd, comment):
        self.matricula_aluno = matricula_aluno
        self.date = date
        self.dateTimeStart = dateTimeStart
        self.dateTimeEnd = dateTimeEnd
        self.comment = comment

    def __repr__(self):
        return '<id {}>'.format(self.id)

class UserSchema(ma.Schema):
  class Meta:
    fields = ('id', 'username', 'email')

class FlightSchema(ma.Schema):
  class Meta:
    fields = ('id', 'matricula_aluno', 'date', 'dateTimeStart', 'dateTimeEnd', 'comment')