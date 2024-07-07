# ecotrueque/models.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Registro(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    usuario = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    contraseña = db.Column(db.String(255), nullable=False)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    genero = db.Column(db.Enum('Masculino', 'Femenino', 'Otros'), nullable=False)

    def __repr__(self):
        return f"<Usuario {self.usuario}: {self.email}>"

class Publicaciones(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(150), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    imagenes = db.Column(db.String(150), nullable=False)
   # imagenes = db.Column(db.LargeBinary)  # Columna para almacenar la imagen como datos binarios

    def __repr__(self):
        return f"<Publicacion {self.id}: {self.titulo}>"




