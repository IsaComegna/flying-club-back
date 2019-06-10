from app import db, ma
from datetime import datetime


class User(db.Model):
  id = db.Column(db.BigInteger(), primary_key=True)
  matricula = db.Column(db.String())
  name = db.Column(db.String(80), unique=True)
  email = db.Column(db.String(120), unique=True)
  user_type = db.Column(db.String())
  cpf = db.Column(db.BigInteger, unique=True)
  phone_number = db.Column(db.String())
  birthday = db.Column(db.Date())


  def __init__(self, matricula, name, email, user_type, cpf, phone_number, birthday):
    self.name = name
    self.matricula = matricula
    self.email = email
    self.user_type = user_type
    self.cpf = cpf
    self.phone_number = phone_number
    self.birthday = birthday

  def persist(self):
    db.session.add(self)
    db.session.commit()

  def __repr__(self):
    return '<User %r>' %self.name

class Flight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    matricula_aluno = db.Column(db.BigInteger())
    registerDate = db.Column(db.Date())
    dateTimeFlightStart = db.Column(db.DateTime())
    dateTimeFlightEnd = db.Column(db.DateTime())
    grade = db.Column(db.Float())
    comment = db.Column(db.Text())

    def __init__(self, matricula_aluno, registerDate, dateTimeFlightStart, dateTimeFlightEnd, comment, grade):
        self.matricula_aluno = matricula_aluno
        self.registerDate = registerDate
        self.dateTimeFlightStart = dateTimeFlightStart
        self.dateTimeFlightEnd = dateTimeFlightEnd
        self.comment = comment
        self.grade = grade

    def persist(self):
      db.session.add(self)
      db.session.commit()

    def __repr__(self):
        return '<id {}>'.format(self.id)

class UserSchema(ma.Schema):
  class Meta:
    fields = ('id', 'matricula', 'name', 'email', 'user_type', 'cpf', 'phone_number', 'birthday')

class FlightSchema(ma.Schema):
  class Meta:
    fields = ('id', 'matricula_aluno', 'registerDate', 'dateTimeFlightStart', 'dateTimeFlightEnd', 'comment', 'grade')