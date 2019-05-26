from app import db, ma
from datetime import datetime


class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), unique=True)
  email = db.Column(db.String(120), unique=True)
  user_type = db.Column(db.String)

  def __init__(self, username, email, user_type):
    self.username = username
    self.email = email
    self.user_type = user_type

  def __repr__(self):
    return '<User %r>' %self.username

class Flight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    matricula_aluno = db.Column(db.String())
    date = db.Column(db.Date())
    dateTimeStart = db.Column(db.Date())
    dateTimeEnd = db.Column(db.Date())
    grade = db.Column(db.Float())
    comment = db.Column(db.Text())

    def __init__(self, matricula_aluno, date, dateTimeStart, dateTimeEnd, comment, grade):
        self.matricula_aluno = matricula_aluno
        self.date = date
        self.dateTimeStart = dateTimeStart
        self.dateTimeEnd = dateTimeEnd
        self.comment = comment
        self.grade = grade

    def __repr__(self):
        return '<id {}>'.format(self.id)

class UserSchema(ma.Schema):
  class Meta:
    fields = ('id', 'username', 'email', 'user_type')

class FlightSchema(ma.Schema):
  class Meta:
    fields = ('id', 'matricula_aluno', 'date', 'dateTimeStart', 'dateTimeEnd', 'comment', 'grade')