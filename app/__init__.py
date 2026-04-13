from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
import os

app = Flask(__name__)
app.config.from_object('app.config.Config')

csrf = CSRFProtect(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

from app import views, models