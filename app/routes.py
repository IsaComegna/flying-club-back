from app import app, db
from flask import Flask, request, jsonify
from app.models import User, Flight, UserSchema, FlightSchema
from flask_cors import CORS
CORS(app)

# initialize schema
user_schema = UserSchema(strict=True)
users_schema =UserSchema(many=True, strict=True)

flight_schema = FlightSchema(strict=True)
flights_schema =FlightSchema(many=True, strict=True)

@app.route('/registro-usuario', methods=['POST'])
def add_user():
  name = request.json['name']
  email = request.json['email']
  user_type = request.json['user_type']
  cpf = request.json['cpf']
  phone_number = request.json['phone_number']
  birthday = request.json['birthday']
  matricula = request.json['cpf']

  new_user = User(matricula, name, email, user_type, cpf, phone_number, birthday)
  db.session.add(new_user)
  db.session.commit()

  return user_schema.jsonify(new_user)

@app.route('/registro-voo', methods=['POST'])
def add_flight():
  matricula_aluno = request.json['matricula_aluno']
  registerDate = request.json['registerDate']
  dateTimeFlightStart = request.json['dateTimeFlightStart']
  dateTimeFlightEnd = request.json['dateTimeFlightEnd']
  comment = request.json['comment']
  grade = request.json['grade']

  new_flight = Flight(matricula_aluno, registerDate, dateTimeFlightStart, dateTimeFlightEnd, comment, grade)
  db.session.add(new_flight)
  db.session.commit()

  return flight_schema.jsonify(new_flight)

@app.route('/voos', methods=['GET'])
def get_flights():
  cols = ['matricula_aluno', 'registerDate', 'dateTimeFlightStart', 'dateTimeFlightEnd', 'grade', 'comment']
  data = Flight.query.all()
  result = [{col: getattr(d, col) for col in cols} for d in data]

  return jsonify(result=result)

@app.route('/voos/<matricula_aluno>', methods=['GET'])
def get_flights_per_student(matricula_aluno):
  cols = ['registerDate', 'dateTimeFlightStart', 'dateTimeFlightEnd', 'grade', 'comment']
  data = Flight.query.filter_by(matricula_aluno=matricula_aluno).all()
  result = [{col: getattr(d, col) for col in cols} for d in data]

  return jsonify(result=result)

@app.route('/usuarios', methods=['GET'])
def get_users():
  cols = ['name', 'matricula', 'email', 'user_type']
  data = User.query.all()
  result = [{col: getattr(d, col) for col in cols} for d in data]

  return jsonify(result=result)

@app.route('/professores', methods=['GET'])
def get_instructors():
  cols = ['name', 'matricula', 'email']
  data = User.query.filter_by(user_type='instructor').all()
  result = [{col: getattr(d, col) for col in cols} for d in data]

  return jsonify(result=result)

@app.route('/alunos', methods=['GET'])
def get_students():
  cols = ['name', 'matricula', 'email']
  data = User.query.filter_by(user_type='student').all()
  result = [{col: getattr(d, col) for col in cols} for d in data]

  return jsonify(result=result)
