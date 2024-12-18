from flask import Flask
from models import db, User, Recipe, UserRecipe, SavedRecipe


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ktenpa:9845@localhost/recipe-database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)