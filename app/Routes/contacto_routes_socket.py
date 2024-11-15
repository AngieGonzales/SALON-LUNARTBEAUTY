from flask import render_template, request, redirect, url_for, flash, Blueprint, jsonify
from app.Models import Contacto  
from app import db

bp = Blueprint('contactsocket', __name__, url_prefix='/contactosockets')

@bp.route('/enviarcontacto', methods=['POST'])
def send_contacto():
    data = request.json
    new_message = Contacto(message=data['message'])
    db.session.add(new_message)
    db.session.commit()
    return jsonify({'message': 'Message created successfully'}), 201