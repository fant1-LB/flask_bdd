from flask import Flask
from app import app
from flask_sqlalchemy import SQLAlchemy
db= SQLAlchemy(app)

class ObjetDuFonds(db.Model):
    __tablename__ ='ObjetDuFonds'
    dossier = db.Column(db.Text(30))
    # dossier = db.Column(db.Text(30), db.ForeignKey('CartonsAN.id'))
    Image = db.Column(db.Text(30), primary_key= True, unique=True)
    Nature = db.Column(db.Text(30))
    # id_contenant_orig = db.Column(db.Text(30), db.ForeignKey('PochettesForbin.id'))
    id_contenant_orig = db.Column(db.Text(30))
    


class PochettesForbin(db.Model):
    __tablename__="PochettesForbin"
    id=db.Column(db.Text(30), primary_key=True, unique=True)
    titre= db.Column(db.Text(50))
    natureDuContenant = db.Column(db.Text(30))

class CartonsAN(db.Model):
    __tablename__ = "CartonsAN"
    id=db.Column(db.Text(30), primary_key=True, unique=True)
    
    titre= db.Column(db.Text(50))
    

