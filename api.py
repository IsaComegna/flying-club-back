from app import app
from app.models import User, Flight, UserSchema, FlightSchema


if __name__ == '__main__':
    app.run()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Flight': Flight}