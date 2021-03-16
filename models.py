from sqlalchemy import Column, String, create_engine
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import json
import os

database_path = os.environ['DATABASE_URL']

db = SQLAlchemy()
'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()
    migrate = Migrate(app, db)

'''
Region
Represents the Region where the environment service is available
'''
class Region(db.Model):
  __tablename__ = 'region'

  id = Column(db.Integer, primary_key=True)
  name = Column(String, unique=True)
  city = Column(String, nullable=False)
  state = Column(String, nullable=False)
  country = Column(String, nullable=False)
  regionhead = Column(String, nullable=False)
  services = db.relationship('Service', backref='region', lazy=True, cascade="delete, merge, save-update")

  def __init__(self, name, city, state, country, regionhead):
    self.name = name
    self.city = city
    self.state = state
    self.country = country
    self.regionhead = regionhead

  def insert(self):
      db.session.add(self)
      db.session.commit()

  def update(self):
      db.session.commit()

  def delete(self):
      db.session.delete(self)
      db.session.commit()

  def format(self):
    return {
        'id': self.id,
        'name': self.name,
        'city': self.city,
        'state': self.state,
        'country': self.country,
        'regionhead': self.regionhead
    }

  def __repr__(self):
      return f'<Region id:{self.id} name:{self.name}, city:{self.city}, ' \
             f'state:{self.state}, country:{self.country}, regionhead:{self.regionhead} >'


'''
Service
Represents the Environment Service
'''
class Service(db.Model):
  __tablename__ = 'service'

  id = Column(db.Integer, primary_key=True)
  name = Column(String, nullable=False)
  type = Column(String, nullable=False)
  address = Column(String, nullable=False)
  email= Column(String)
  phone = Column(String)
  website = Column(String)
  image = Column(String)
  region_id = db.Column(db.Integer, db.ForeignKey('region.id'), nullable=False)

  def __init__(self, name, type, address, region_id, email=None, phone=None, website=None, image=None):
    self.name = name
    self.type = type
    self.address = address
    self.email = email
    self.phone = phone
    self.website = website
    self.image = image
    self.region_id = region_id

  def insert(self):
      db.session.add(self)
      db.session.commit()

  def update(self):
      db.session.commit()

  def delete(self):
      db.session.delete(self)
      db.session.commit()

  def format(self):
    return {
        'id': self.id,
        'name': self.name,
        'type': self.type,
        'address': self.address,
        'region_id': self.region_id,
        'email': self.email,
        'phone': self.phone,
        'website': self.website,
        'image': self.image
    }

  def __repr__(self):
      return f'<id:{self.id} name:{self.name}, type:{self.type}, ' \
             f'address:{self.address}, email:{self.email}, ' \
             f'phone:{self.phone}, website:{self.website}, image:{self.image} >'

