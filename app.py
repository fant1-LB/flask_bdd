from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug=True

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

from models.database import *

def init_db():
    db.create_all()
    



if __name__ == '__main__':
    with app.app_context():
        init_db()
    app.run()