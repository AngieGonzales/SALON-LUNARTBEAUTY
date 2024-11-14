import pytest
from app import create_app, db
from app.Models.contacto import Contacto
from flask import url_for


def test_enviar_contacto_get(client):
    response = client.get('/enviar_contacto')
    assert response.status_code == 200
    assert b"Contacto" in response.data

def test_enviar_contacto_post_success(client, app):
    with app.app_context():
        data = {
            'message': 'Este es un mensaje de prueba'
        }
        response = client.post('/enviar_contacto', data=data, follow_redirects=True)
        assert response.status_code == 200
        assert b"Mensaje enviado correctamente" in response.data

        # Verificar que el mensaje se ha añadido a la base de datos
        contacto = Contacto.query.filter_by(message='Este es un mensaje de prueba').first()
        assert contacto is not None

def test_enviar_contacto_post_error(client, app, monkeypatch):
    def mock_commit_error(*args, **kwargs):
        raise Exception("Error de prueba")

    with app.app_context():
        monkeypatch.setattr(db.session, "commit", mock_commit_error)

        data = {
            'message': 'Este mensaje debería fallar'
        }
        response = client.post('/enviar_contacto', data=data, follow_redirects=True)
        assert response.status_code == 200
        assert b"Error al enviar el mensaje" in response.data

        # Verificar que el mensaje no se ha añadido a la base de datos
        contacto = Contacto.query.filter_by(message='Este mensaje debería fallar').first()
        assert contacto is None

def test_contacto_model( app):
    with app.app_context():
        contacto = Contacto(message='contact')
        db.session.add(contacto)
        db.session.commit()

        recuperado = Contacto.query.filter_by(message='contact').first()
        assert recuperado is not None
        assert recuperado.message == 'contac'
