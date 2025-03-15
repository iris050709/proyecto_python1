from flask import Flask
from config import db,migrate
from routes.user import user_bp
from dotenv import load_dotenv
import os
from flask_cors import CORS
from flask_jwt_extended import JWTManager

load_dotenv()

app= Flask(__name__)
CORS(app)
app.config['JWT_SECRET_KEY'] = 'Hoy desperte pensando en ti chakira'
jwt = JWTManager(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/prueba'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate.init_app(app,db)

from routes.user import user_bp
app.register_blueprint(user_bp,url_prefix='/users')

if __name__ == '__main__':
    app.run(debug=True)