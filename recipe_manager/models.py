import bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model, UserMixin):
   id = db.Column(db.Integer, primary_key=True)
   username = db.Column(db.String(150), nullable=False, unique=True)
   password = db.Column(db.String(150), nullable=False)

   def set_password(self, password):
       """Hash the password before saving it to the database."""
       self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

   def check_password(self, password):
       """Check if the given password matches the hashed password."""
       return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    content = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer)  # New rating field


def connect_db(app):
    """Connect this database to Flask app"""

    db.app = app
    db.init_app(app)
