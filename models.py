from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Episode(db.Model):
    __tablename__ = 'episodes'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String, nullable=False)  
    number = db.Column(db.String, nullable=False)  
    appearances = db.relationship('Appearance', back_populates='episode', cascade="all, delete")

class Guest(db.Model):
    __tablename__ = 'guests'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    occupation = db.Column(db.String, nullable=False)
    appearances = db.relationship('Appearance', back_populates='guest', cascade="all, delete")
