# /run.py
import os

from src.app import create_app


def set_environment_variables():
    """
    This section method is modified from the tutorial, because the tutorial wants you to set environment variables
    via the terminal. Given that we're running within Docker, I am setting these variables in Python instead,
    """
    os.environ["FLASK_ENV"] = 'development'
    os.environ["DATABASE_URL"] = 'postgres://test:password@example:5432/blog_api_db'
    os.environ["JWT_SECRET_KEY"] = 'hhgaghhgsdhdhdd'


if __name__ == '__main__':
    env_name = os.getenv('FLASK_ENV')

    if env_name is None:
        env_name = 'development'

    app = create_app(env_name)
    # run app
    app.run()
