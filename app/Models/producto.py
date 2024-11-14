from app import db


class Producto(db.Model):
    __tablename__ = 'producto'
    
    idproducto = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    precio = db.Column(db.Float, nullable=False)  # Cambiado a Float
    imagen=db.Column(db.String(255), nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.idCategoria'))
    stock = db.Column(db.Integer, default=0)

    # Relaciones
    categorias = db.relationship("Categoria", back_populates="productoss")
    carrito = db.relationship('Carrito', back_populates='producto')  # Cambié aquí


def get_id(self):
       return str(self.id)
    
    
def to_dict(self):
        return{
            "idprodcuto": self.idproducto,
            "precio": self.precio,
            "imagen": self.imagen,
            "categoria_id": self.categoria_id,
            "stock": self.stock,
           
        }