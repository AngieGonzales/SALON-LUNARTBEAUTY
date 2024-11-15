from app import db

class Contacto(db.Model):
    __tablename__ = 'contacto'
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text, nullable=False)

    def get_id(self):
        return str(self.id)
    
    
    def to_dict(self):
        return{
            "id": self.id,
            "message": self.message
        }