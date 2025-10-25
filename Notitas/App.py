from flask import Flask, render_template, request, redirect, url_for
from models.nota import db, Nota

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notitas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def index():
  notas = Nota.query.order_by(Nota.fecha_creacion.desc()).all()
  return render_template("index.html", notas=notas)