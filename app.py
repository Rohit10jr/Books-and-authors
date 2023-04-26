from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


app = Flask(__name__)
# db_confi[ pilml8p;[9]] = yaml.safe_load(open('database.yaml'))
SQLALCHEMY_DATABASE_URI = 'sqlite:///./test.db'
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)
CORS(app)