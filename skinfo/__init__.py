
import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

with open("./config.json", 'r') as file:
    config = json.loads(file.read())

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.sqlite"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "asecretkey"

db = SQLAlchemy(app)
with app.app_context():
    db.create_all()
    
from skinfo import routes