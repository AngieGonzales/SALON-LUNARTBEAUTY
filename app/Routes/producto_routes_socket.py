from flask import Blueprint, render_template, request, redirect, url_for, jsonify, send_file
from app.Models.producto import Producto
from app import db
from io import BytesIO
import base64
import json


bp = Blueprint('prodcutosocket', __name__, url_prefix='/Productosockets')


@bp.route('/index/producto', methods=['GET'])
def get_users():
    productos = Producto.query.all()
    return jsonify([{
        'idproducto': producto.idproducto,
        'nombre': producto.nombre,
        'imagen': producto.imagen,
        'categoria_id': producto.categoria_id,
        'stok': producto.stock
    } for producto in productos]), 200, {'Content-Type': 'application/json'}


@bp.route('/add/producto', methods=['POST'])
def create_user():
    print("entra a create")
    data = request.json
    new_prodcuto = Producto(nombre=data['nombre'], precio =data['precio'],  imagen =data['imagen'],  categoria_id =data['categoria_id '],  stock =data[' stok'],  rol =data['rol'] )
    db.session.add(new_prodcuto)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201


@bp.route('/update/producto/<int:id>', methods=['PUT'])
def update_user(id):
    producto = Producto.query.get(id)
    if producto:
        data = request.json
        producto.nombre = data['nombre']
        producto.precio = data['precio']
        producto.imagen = data['imagen']
        producto.categoria_id = data['categotia_id']
        db.session.commit()
        # Notifica a todos los clientes conectados sobre la actualización
        return jsonify({'message': 'User updated successfully'})
    return jsonify({'message': 'User not found'}), 404



@bp.route('/delete/producto/<int:id>', methods=['DELETE'])
def delete_user(id):
    print("entra de delete")
    producto = Producto.query.get(id)
    if producto:
        db.session.delete(producto)
        db.session.commit()
        return jsonify({'message': 'User deleted successfully'})
    return jsonify({'message': 'User not found'}), 404

