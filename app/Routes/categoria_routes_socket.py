from flask import Blueprint, render_template, request, jsonify
from app.Models.categoria import Categoria
from app import db

bp = Blueprint('categoriasocket', __name__, url_prefix='/Categoriasockets')


@bp.route('/index/categoria', methods=['GET'])
def get_categoria():
    categorias = Categoria.query.all()
    return jsonify([
        {
            'idCategoria': categoria.idCategoria,
            'nombre': categoria.nombre,
            'descripcion': categoria.descripcion,
            'imagen': categoria.imagen
        } for categoria in categorias
    ]), 200


@bp.route('/add/categoria', methods=['POST'])
def create_categoria():
    data = request.json
    new_categoria = Categoria(
        nombre=data['nombre'],
        descripcion=data['descripcion'],
        imagen=data['imagen']
    )
    db.session.add(new_categoria)
    db.session.commit()
    return jsonify({'message': 'Categoría creada correctamente'}), 201


@bp.route('/update/categoria/<int:id>', methods=['PUT'])
def update_categoria(id):
    categoria = Categoria.query.get(id)
    if categoria:
        data = request.json
        categoria.nombre = data['nombre']
        categoria.descripcion = data['descripcion']
        categoria.imagen = data['imagen']
        db.session.commit()
        return jsonify({'message': 'Categoría actualizada correctamente'})
    return jsonify({'message': 'Categoría no encontrada'}), 404


@bp.route('/delete/categoria/<int:id>', methods=['DELETE'])
def delete_categoria(id):
    categoria = Categoria.query.get(id)
    if categoria:
        db.session.delete(categoria)
        db.session.commit()
        return jsonify({'message': 'Categoría eliminada correctamente'})
    return jsonify({'message': 'Categoría no encontrada'}), 404
