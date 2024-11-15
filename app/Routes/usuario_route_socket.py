from flask import Blueprint, render_template, request, redirect, url_for, jsonify, send_file
from app.Models.usuario import Usuario
from app import db
from io import BytesIO
import base64
import json

bp = Blueprint('usuariosocket', __name__, url_prefix='/Usuariosockets')

@bp.route('/index', methods=['GET'])
def get_users():
    usuario = Usuario.query.all()
    return jsonify([{'id': usuario.id, 'nombre': usuario.nombre, 'apellido': usuario.apellido, 'celular': usuario.celular,   'correo': usuario.correo,  'fecha_nacimiento': usuario.fecha_nacimiento,  'rol': usuario.rol, 'pass': usuario.password_hash } for usuario in usuario]), 200, {'Content-Type': 'application/json'}


@bp.route('/add', methods=['POST'])
def create_user():
    data = request.json
    new_user = Usuario(nombre=data['nombre'], apellido=data['apellido'],  celular =data['celular'],  correo =data['correo'],  fecha_nacimiento =data['fecha_nacimiento'], rol =data['rol'],  password_hash=data['password_hash']  )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201


@bp.route('/update/<int:id>', methods=['PUT'])
def update_user(id):
    usuario = Usuario.query.get(id)
    if usuario:
        data = request.json
        usuario.nombre = data['nombre']
        usuario.apellido = data['apellido']
        usuario.celular = data['celular']
        usuario.correo = data['correo']
        usuario.fecha_nacimiento = data['fecha_nacimiento']
        usuario.rol = data['rol']
        usuario.password_hash = data['password_hash']
        db.session.commit()
        # Notifica a todos los clientes conectados sobre la actualización
        return jsonify({'message': 'User updated successfully'})
    return jsonify({'message': 'User not found'}), 404



@bp.route('/delete/<int:id>', methods=['DELETE'])
def delete_user(id):
    print("entra de delete")
    usuario = Usuario.query.get(id)
    if usuario:
        db.session.delete(usuario)
        db.session.commit()
        return jsonify({'message': 'User deleted successfully'})
    return jsonify({'message': 'User not found'}), 404

