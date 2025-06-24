from flask import Flask
from app import app
from flask_sqlalchemy import SQLAlchemy
db= SQLAlchemy(app)

class ObjetDuFonds(db.Model):
    __tablename__ ='ObjetDuFonds'
    id = db.Column(db.Integer, primary_key=True)
    dossier_conserv_AN = db.Column(db.Text(30))
    # dossier = db.Column(db.Text(30), db.ForeignKey('CartonsAN.id'))
    prise_de_vue = db.Column(db.Text(30), unique = True)
    nature_de_l_objet_physique = db.Column(db.Text(30))
    # id_contenant_orig = db.Column(db.Text(30), db.ForeignKey('PochettesForbin.id'))
    desc_contenant_orig = db.Column(db.Text(30))
    
# ObjetCoteImage = db.Table ("ObjetCoteImage"), db.metadata, db.Column ("ObjetID", db.Integer, db.ForeignKey('ObjetDuFonds.id')), db.Column("ImageID")
# voir https://medium.com/@garg10may/sqlalchemy-many-to-many-ce7987f17c79 pour le modèle many to many


class ObjetCoteImage(db.Model):
    __tablename__ = 'ObjetCoteImage'
    id = db.Column(db.Integer, primary_key=True)
    objet_correspondant = db.Column(db.Text(30), db.ForeignKey('ObjetDuFonds.prise_de_vue'))
    image_correspondate = db.Column(db.Text(30), db.ForeignKey('ImageConcept.id'))

class ImageConcept(db.Model):
    __tablename__ = 'ImageConcept'
    id=db.Column(db.Integer, primary_key=True)
    evenement=db.Column(db.Text(30))
    caption=db.Column(db.Text(30))
    
