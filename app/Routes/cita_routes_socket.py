from flask import Blueprint, render_template, request, redirect, url_for, jsonify, send_file
from app.Models.cita import Cita
from app import db
from io import BytesIO
import base64
import json


bp = Blueprint('citasocket', __name__, url_prefix='/Citasockets')


@bp.route('/index/cita', methods=['GET'])
def get_cita():
    cita = Cita.query.all()
    return jsonify([{
        'idcita': cita.idcita,
        'fecha': cita.fecha,
        'hora': cita.hora,
        'cliente': cita.cliente,
        'servicio_id': cita.servicio_id,
        'estilista_id': cita.estilista_id,
        
    } for cita in cita]), 200, {'Content-Type': 'application/json'}



@bp.route('/add/cita', methods=['POST'])
def create_cita():
    print("entra a create")
    data = request.json
    new_cita= Cita(fecha=data['fecha'], hora =data['hora'], cliente =data['cliente'], servicio_id =data['servicio_id'],  estilista_id =data[' estilista_id'] ) 
    db.session.add(new_cita)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201




@bp.route('/update/cita/<int:id>', methods=['PUT'])
def update_estilista(id):
    cita = Cita.query.get(id)
    if  cita:
        data = request.json
        cita.fecha = data['fecha']
        cita.hora = data['hora']
        cita.cliente = data['cliente']
        cita.servicio_id = data['servicio_id']
        cita.estilista_id = data['estilista_id']
        db.session.commit()
        # Notifica a todos los clientes conectados sobre la actualización
        return jsonify({'message': 'User updated successfully'})
    return jsonify({'message': 'User not found'}), 404



@bp.route('/delete/cita/<int:id>', methods=['DELETE'])
def delete_cita(id):
    print("entra de delete")
    cita = Cita.query.get(id)
    if cita:
        db.session.delete(cita)
        db.session.commit()
        return jsonify({'message': 'User deleted successfully'})
    return jsonify({'message': 'User not found'}), 404
