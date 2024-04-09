from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from dotenv import load_dotenv
from sqlalchemy.orm import DeclarativeBase

load_dotenv()  # take environment variables from .env.

app = Flask(__name__)

app.config.from_object(Config)

db = SQLAlchemy(model_class=DeclarativeBase)
db.init_app(app)

from app import views