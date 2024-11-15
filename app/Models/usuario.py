from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

class Usuario(db.Model, UserMixin):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    celular = db.Column(db.String(10), nullable=False)
    correo = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    fecha_nacimiento = db.Column(db.String(30), nullable=False)
    rol = db.Column(db.String(20), nullable=False)  
    

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
  
      return check_password_hash(self.password_hash, password)
  
    def get_id(self):
        return str(self.id)
    
    
    def to_dict(self):
        return{
            "id": self.id,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "celular": self.celular,
            "correo": self.correo,
            "fecha_nacimiento": self.fecha_nacimiento,
            "rol": self.rol,
            "password_hash": self.password_hash,
        }