import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy

from src.app import create_app, db

# from src.models import db


env_name = os.getenv('FLASK_ENV')
app = create_app('development')
#app = create_app('env_name')

# db.init_app(app)
migrate = Migrate(app=app, db=db)

manager = Manager(app=app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
