from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

@app.route("/")
def home():
    return "PostgreSQL bağlantısı başarılı!"

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask ve PostgreSQL'e hoş geldiniz!"

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def hello_world():
    return 'Hello, World!'

