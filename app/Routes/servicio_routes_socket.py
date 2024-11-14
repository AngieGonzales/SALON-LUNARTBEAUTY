from flask import Blueprint, render_template, request, redirect, url_for, jsonify, send_file
from app.Models.servicio import Servicio
from app import db
from io import BytesIO
import base64
import json


bp = Blueprint('serviciosocket', __name__, url_prefix='/Serviciosockets')


@bp.route('/index/servicio', methods=['GET'])
def get_servicios():
    servicios = Servicio.query.all()
    return jsonify([{
        'idservicio': servicio.idservicio,
        'nombre': servicio.nombre,
        'descripcion': servicio.descripcion,
        'imagen': servicio.imagen,
    } for servicio in servicios]), 200, {'Content-Type': 'application/json'}



@bp.route('/add/servicio', methods=['POST'])
def create_servicio():
    print("entra a create")
    data = request.json
    new_servicio = Servicio(nombre=data['nombre'], descripcion=data['descripcion'],  imagen =data['imagen']  )
    db.session.add(new_servicio)
    db.session.commit()
    return jsonify({'message': 'Servicio creado exitosamente'}), 201


@bp.route('/update/servicio/<int:id>', methods=['PUT'])
def update_servicio(id):
    servicio= Servicio.query.get(id)
    if servicio:
        data = request.json
        Servicio.nombre = data['nombre']
        Servicio.descripcion = data['descripcion']
        Servicio.imagen = data['imagen']
        db.session.commit()
        # Notifica a todos los clientes conectados sobre la actualización
        return jsonify({'message': 'Servicio actualizado exitosamente'})
    return jsonify({'message': 'Servicio no encontrado'}), 404



@bp.route('/delete/servicio/<int:id>', methods=['DELETE'])
def delete_servicio(id):
    print("entra de delete")
    servicio = Servicio.query.get(id)
    if servicio:
        db.session.delete(servicio)
        db.session.commit()
        return jsonify({'message': 'Servicio eliminado exitosamente'})
    return jsonify({'message': 'Servicio no encontrado'}), 404

