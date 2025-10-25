from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Nota(db.Model):
  __tablename__= "notas"

  id = db.Column(db.Integer, primary_key=True)
  titulo = db.Column(db.String(100), nullable=False)
  contenido = db.Column(db.Text, nullable=False)
  fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)

  def __repr__(self):
    return f'<nota {self.id} - {self.titulo}>'
  
"""
db = SQLAlchemy() → prepara la conexión con la base (la app la activará después).

class Nota(db.Model) → define la estructura de una nota, equivalente a una tabla SQL.
__tablename__ → opcional, solo para controlar el nombre de la tabla.
id, titulo, contenido, fecha_creacion → las columnas.
__repr__ → ayuda a ver algo legible cuando inspeccionas una nota en consola.
"""