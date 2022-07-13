import re
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, TextAreaField, SelectField
from wtforms.validators import InputRequired, Optional, NumberRange, URL, Regexp

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Pet(db.Model):

    __tablename__ = 'pets'

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    name = db.Column(db.String(50),
                     nullable=False,
                     )
    species = db.Column(db.Text,
                        nullable=False,
                        )
    age = db.Column(db.Integer,
                    nullable=True
                    )
    image_url = db.Column(db.Text,
                          nullable=True
                          )
    notes = db.Column(db.Text,
                      nullable=True
                      )
    available = db.Column(db.Boolean,
                          default=True)
                          

class AddPetForm(FlaskForm):
    name = StringField('name', validators=[InputRequired()])
    species = SelectField('species', 
                          choices=(['Cat', 'Cat'],
                                    ['Dog', 'Dog'],
                                    ['Porcupine', 'Porcupine'])
                          
    )
                          
    age = IntegerField('age',
                        validators=[InputRequired(),
                                    NumberRange(min=0, max=30, message='age out of range')])
    image_url = StringField('image_url',
                            validators=[Optional(), URL()])
    notes = TextAreaField('notes',
                          validators=[Optional()])
    available = BooleanField('avaialable')

                          
    