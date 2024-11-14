from app import db

class Servicio(db.Model):
    __tablename__='servicio'
    idservicio = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    descripcion=db.Column(db.String(255), nullable=False)
    imagen=db.Column(db.String(255), nullable=False)
   
    cita = db.relationship('Cita', back_populates='servicio')
    
    
    
def get_id(self):
        return str(self.id)
    
    
def to_dict(self):
        return{
            "idservicio": self.idservicio,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "iamgen": self.imagen,
        }