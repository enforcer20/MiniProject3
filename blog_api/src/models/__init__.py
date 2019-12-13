# src/models/__init__.py

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


#from .UserModel import UserModel, UserSchema
#from .BlogpostModel import BlogpostModel, BlogpostSchema

# initialize our db
db = SQLAlchemy()
bcrypt = Bcrypt()
