# flying-club-back

## Disclaimer
 This app is ment to be used as an API for a Flight School.

## Running app locally:
- Make sure you have Python installed
- Install pip
- Create a virtual env
- Install the packages listed on requirements.txt through pip
- Export the paths necessary to the application
  - export DATABASE_URL='postgresql://<user>:<password>@localhost/flying-club'
  - export FLASK_APP=api.py
  - export APP_SETTINGS="config.DevelopmentConfig"
- Create the database
  - $ python
  - $ from app import db
  - $ db.create_all()
- Run "flask run"

## The app is deployed on Heroku at the following url:
  https://flying-club-engesoft.herokuapp.com/
