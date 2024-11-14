import pytest
from app import create_app, db
from app.Models.estilista import Estilista

def test_index(client):
    response = client.get('/estilista')
    assert response.status_code == 200
    assert b'LISTA DE ESTILISTAS' in response.data

def test_add_estilista(client):
    response = client.post('/agregar-estilistas', data={
        'nombre': 'Juan Pérez',
        'telefono': '1234567890'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'estilistas' in response.data


def test_edit_estilista(client):
    estilista = Estilista(nombre='María García', telefono='0987654321')
    with client.application.app_context():
        db.session.add(estilista)
        db.session.commit()
        estilista_id = estilista.idEstilista

    response = client.post(f'/estilista/edit/{estilista_id}', data={
        'nombre': 'María López',
        'telefono': '1122334455'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'estilistas' in response.data


def test_delete_estilista(client):
    estilista = Estilista(nombre='Carlos Rodríguez', telefono='5566778899')
    with client.application.app_context():
        db.session.add(estilista)
        db.session.commit()
        estilista_id = estilista.idEstilista

    response = client.get(f'/estilista/delete/{estilista_id}', follow_redirects=True)
    assert response.status_code == 200
    assert b'dataE' not in response.data