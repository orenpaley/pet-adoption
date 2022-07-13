from email.mime import image
from flask import Flask, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import connect_db, Pet, AddPetForm, db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_adoption'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "jjF73!rtc"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = '1sdAagieDndiJ7364k'
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def home():
  """ Home page where user can see full table of pets in database"""
  pets = Pet.query.all()
  return render_template('home.html', pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def add_pet():
  """ add pet from """
  form = AddPetForm()
  if form.validate_on_submit():
    name = form.name.data
    age = form.age.data
    species = form.species.data
    image_url = form.image_url.data
    notes = form.notes.data
    available = form.available.data

    pet = Pet(name=name,
             age=age, 
             species=species, 
             image_url=image_url, 
             notes=notes, 
             available=available)

    db.session.add(pet)
    db.session.commit()
   

    return redirect('/')

  else:
    return render_template('add.html', form=form)

@app.route('/<id>', methods=['GET', 'POST'])
def pet_details(id):
  """ pet details with form to update"""
  pet = Pet.query.get_or_404(id)
  form = AddPetForm(obj=pet)

  if form.validate_on_submit():
    pet.name = form.name.data
    pet.age = form.age.data
    pet.species = form.species.data
    pet.image_url = form.image_url.data
    pet.notes = form.notes.data
    pet.available = form.available.data
    db.session.commit()
    return redirect('/')


  return render_template('pet.html', form=form, pet=pet)

