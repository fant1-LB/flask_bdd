from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug=True
#Modifier ci dessous pour modifier le nom de la base
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
#Importer les fonctions et le modèle de la base
from models.database import *
from utils.fonctions import *
importer_ou_pas = True
nom_csv = "donnees_boites2_260.csv"
nom_table = "ObjetDuFonds"


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        if importer_ou_pas:
            print("import de donnée")
            add_to_database(nom_csv, nom_table, db)
        
    app.run()