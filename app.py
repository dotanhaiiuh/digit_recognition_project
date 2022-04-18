from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = ''
    # postgresql://postgres:123456@localhost
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/tfjs')
def index():
    return render_template('tfjs.html')

@app.route('/')
def hello_world():
    return render_template('index.html')
if __name__ == "__main__":
    app.debug = True
    app.run()