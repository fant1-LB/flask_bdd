from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug=True

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

from models.database import *
from utils.fonctions import *
importer_ou_pas = True
nom_csv = "test1.csv"
nom_table = "CartonsAN"


if __name__ == '__main__':
    with app.app_context():
        
        db.create_all()
        if importer_ou_pas:
            add_to_database(nom_csv, nom_table, db)
        
    app.run()