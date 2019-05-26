from app import app, db
from flask import Flask, request, jsonify
from app.models import User, Flight, UserSchema, FlightSchema


# initialize schema
user_schema = UserSchema(strict=True)
users_schema =UserSchema(many=True, strict=True)

flight_schema = FlightSchema(strict=True)
flights_schema =FlightSchema(many=True, strict=True)

@app.route('/user', methods=['POST'])
def add_user():
  username = request.json['username']
  email = request.json['email']
  user_type = request.json['user_type']

  new_user = User(username, email, user_type)
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
  grade = request.json['grade']

  new_flight = Flight(matricula_aluno, date, dateTimeStart, dateTimeEnd, comment, grade)
  db.session.add(new_flight)
  db.session.commit()

  return flight_schema.jsonify(new_flight)
