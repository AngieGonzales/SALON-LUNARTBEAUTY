import pytest
from app import create_app, db
from app.Models.servicio import Servicio
from io import BytesIO


def test_index_servicios(client):
    response = client.get('/servicio')
    assert response.status_code == 200

def test_index_admin_servicios(client):
    response = client.get('/servicioadmin')
    assert response.status_code == 200

def test_add_servicio(client):
    data = {
        'nombre': 'Servicio de prueba',
        'descripcion': 'Descripción del servicio de prueba',
        'imagen': (BytesIO(b'mi imagen de prueba'), 'test.jpg')
    }
    response = client.post('/servicio/add', data=data, content_type='multipart/form-data')
    assert response.status_code == 302
    
    with client.application.app_context():
        servicio = Servicio.query.filter_by(nombre='Servicio de prueba').first()
        assert servicio is not None
        assert servicio.descripcion == 'Descripción del servicio de prueba'
        assert servicio.imagen == 'test.jpg'

def test_edit_servicio(client):
    servicio = Servicio(nombre='Servicio original', descripcion='Descripción original', imagen='original.jpg')
    with client.application.app_context():
        db.session.add(servicio)
        db.session.commit()
        servicio_id = servicio.idservicio

    data = {
        'nombre': 'Servicio actualizado',
        'descripcion': 'Descripción actualizada',
        'imagen': (BytesIO(b'nueva imagen de prueba'), 'nueva.jpg')
    }
    response = client.post(f'/servicio/edit/{servicio_id}', data=data, content_type='multipart/form-data')
    assert response.status_code == 302

    with client.application.app_context():
        servicio_actualizado = Servicio.query.get(servicio_id)
        assert servicio_actualizado.nombre == 'Servicio actualizado'
        assert servicio_actualizado.descripcion == 'Descripción actualizada'
        assert servicio_actualizado.imagen == 'nueva.jpg'

def test_delete_servicio(client):
    servicio = Servicio(nombre='Servicio a eliminar', descripcion='Descripción', imagen='eliminar.jpg')
    with client.application.app_context():
        db.session.add(servicio)
        db.session.commit()
        servicio_id = servicio.idservicio

    response = client.get(f'/servicio/delete/{servicio_id}')
    assert response.status_code == 302
    assert b'servicio' in response.data

