
from models import db, Pet
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Pet.query.delete()


wiggles = Pet(name='Wiggles', species='Cat', age=10, notes='a playful feller.')
starry = Pet(name='Starry', species='Porcupine', age=4, notes='quiet, curious, stargazer')
Rhonda = Pet(name='Rhonda', species='Dog', age=10, notes='a playful feller.')

db.session.add(wiggles)
db.session.add(starry)
db.session.add(Rhonda)

db.session.commit()