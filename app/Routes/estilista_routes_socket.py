from flask import Blueprint, render_template, request, redirect, url_for, jsonify, send_file
from app.Models.estilista import Estilista
from app import db
from io import BytesIO
import base64
import json


bp = Blueprint('estilistasocket', __name__, url_prefix='/Estilistasockets')


@bp.route('/index/estilista', methods=['GET'])
def get_estilistas():
    estilistas = Estilista.query.all()
    return jsonify([{
        'idEstilista': estilista.idEstilista,
        'nombre': estilista.nombre,
        'telefono': estilista.telefono
        
    } for estilista in estilistas]), 200, {'Content-Type': 'application/json'}



@bp.route('/add/estilista', methods=['POST'])
def create_estilista():
    print("entra a create")
    data = request.json
    new_estilista = Estilista(nombre=data['nombre'], telefono =data['telefono'] )
    db.session.add(new_estilista)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201


@bp.route('/update/estilista/<int:id>', methods=['PUT'])
def update_estilista(id):
    estilista = Estilista.query.get(id)
    if  estilista:
        data = request.json
        estilista.nombre = data['nombre']
        estilista.telefono = data['telefono']
        db.session.commit()
        # Notifica a todos los clientes conectados sobre la actualización
        return jsonify({'message': 'User updated successfully'})
    return jsonify({'message': 'User not found'}), 404




@bp.route('/delete/estilista/<int:id>', methods=['DELETE'])
def delete_estilista(idEstilista):
    print("entra de delete")
    estilista = Estilista.query.get(idEstilista)
    if estilista:
        db.session.delete(estilista)
        db.session.commit()
        return jsonify({'message': 'User deleted successfully'})
    return jsonify({'message': 'User not found'}), 404
