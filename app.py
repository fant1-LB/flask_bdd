from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug=True
#Modifier ci dessous pour modifier le nom de la base
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///highvision.db'
#Importer les fonctions et le modèle de la base
from models.database import *
from utils.fonctions import *

importer_ou_pas = True
liste_csv_pour_import = ["donnees_boites1.csv","donnees_boites2_260.csv"]
liste_tables_pour_import = ["ObjetDuFonds","ObjetDuFonds"]


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        if importer_ou_pas:
            print("import de donnée")
            mass_add_to_database(liste_csv_pour_import, liste_tables_pour_import, db)
        
    app.run()