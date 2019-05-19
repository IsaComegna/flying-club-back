from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

#init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

#database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/flying-club'
app.config['SQLACHEMY_TRACK_MODIFICATIONS'] = False
#init db
db = SQLAlchemy(app)
#init marshmallow
ma = Marshmallow(app)


# classes
class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), unique=True)
  email = db.Column(db.String(120), unique=True)

  def __init__(self, username, email):
    self.username = username
    self.email = email

  def __repr__(self):
    return '<User %r>' %self.username

class UserSchema(ma.Schema):
  class Meta:
    fields = ('id', 'username', 'email')


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

class FlightSchema(ma.Schema):
  class Meta:
    fields = ('id', 'matricula_aluno', 'date', 'dateTimeStart', 'dateTimeEnd', 'comment')

# init schema
user_schema = UserSchema(strict=True)
users_schema =UserSchema(many=True, strict=True)

flight_schema = FlightSchema(strict=True)
flights_schema =FlightSchema(many=True, strict=True)

# routes
@app.route('/user', methods=['POST'])
def add_user():
  username = request.json['username']
  email = request.json['email']

  new_user = User(username, email)
  db.session.add(new_user)
  db.session.commit()

  return user_schema.jsonify(new_user)

@app.route('/voo', methods=['POST'])
def add_flight():
  matricula_aluno = request.json['matricula_aluno']
  date = request.json['date']
  dateTimeStart = request.json['dateTimeStart']
  dateTimeEnd = request.json['dateTimeEnd']
  comment = request.json['comment']

  new_flight = Flight(matricula_aluno, date, dateTimeStart, dateTimeEnd, comment)
  db.session.add(new_flight)
  db.session.commit()

  return flight_schema.jsonify(new_flight)

#run server
if __name__ == '__main__':
  app.run()