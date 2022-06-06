# Models.
#----------------------------------------------------------------------------#
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()
class Venue(db.Model):
    __tablename__ = 'venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    city = db.Column(db.String(120),  nullable=False)
    state = db.Column(db.String(120),  nullable=False)
    address = db.Column(db.String(120),  nullable=False)
    phone = db.Column(db.String(120),  nullable=False)
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    # fields I added
    website = db.Column(db.String(120))
    genres = db.Column(db.ARRAY(db.String), default=[], nullable=False)
    seeking_talent = db.Column(db.Boolean, default=False)
    seeking_description = db.Column(db.String(200))

    show = db.relationship('Show', backref='venue', lazy=True)

class Artist(db.Model):
    __tablename__ = 'artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String,  nullable=False)
    city = db.Column(db.String(120),  nullable=False)
    state = db.Column(db.String(120),  nullable=False)
    phone = db.Column(db.String(120),  nullable=False)
    genres = db.Column(db.ARRAY(db.String), default=[],  nullable=False)
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website = db.Column(db.String(120))
    seeking_venue = db.Column(db.Boolean, default=False)
    seeking_description = db.Column(db.String(200))

    show = db.relationship('Show', backref='artist', lazy=True)



class Show(db.Model):
  __tablename__ = 'show'
  id = db.Column(db.Integer, primary_key=True)
  artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'))
  venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'))
  # artist_image_link = db.Column(db.String(1000))
  start_time = db.Column(db.DateTime, default=datetime.now(), nullable=False)