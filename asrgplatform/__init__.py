from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from dotenv import load_dotenv
from pathlib import Path
from pino import pino
import os

# logger
logger = pino()

# load env config
env_path = Path('../.env')
load_dotenv(dotenv_path=env_path)

# load database
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PW = os.getenv("POSTGRES_PW")
POSTGRES_URL = os.getenv("POSTGRES_URL")
POSTGRES_DB = os.getenv("POSTGRES_DB")
DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
    user=POSTGRES_USER, pw=POSTGRES_PW, url=POSTGRES_URL, db=POSTGRES_DB)

logger.info("[+] init app")
app = Flask(__name__, template_folder="templates", static_folder="static")
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# database stuff
db = SQLAlchemy(app)
db.create_all()
db.session.commit()

# Login Manager
login_manager = LoginManager()
login_manager.init_app(app)


@app.cli.command('resetdb')
def resetdb():
    from sqlalchemy_utils import database_exists, create_database, drop_database
    if database_exists(DB_URL):
        logger.info("[+] dropping database")
        drop_database(DB_URL)
    if not database_exists(DB_URL):
        logger.info("[+] creating database")
        create_database(DB_URL)

    db.create_all()


# register all blueprints
from asrgplatform.main import main as main_bp
app.register_blueprint(main_bp)

from asrgplatform.auth import auth as auth_bp
app.register_blueprint(auth_bp)


import asrgplatform.auth
