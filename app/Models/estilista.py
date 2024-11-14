from app import db

class Estilista(db.Model):

    __tablename__ = 'estilista'
    idEstilista = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    telefono =db.Column(db.String(255), nullable=False)
   
    cita = db.relationship('Cita', back_populates='estilista')
    
    
    
    
def get_id(self):
        return str(self.id)
    
    
def to_dict(self):
        return{
            "idEstilista": self.idEstilista,
            "nombre": self.nombre,
            "telefono": self.telefono,
            
        } 