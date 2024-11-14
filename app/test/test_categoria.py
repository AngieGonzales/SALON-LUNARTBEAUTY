import pytest
from app.Models.categoria import Categoria
from app import db
import io


def test_index(client):
    response = client.get('/categoria/admin')
    assert response.status_code == 200
    assert b'CATEGORIAS' in response.data

def test_index_cliente(client):
    response = client.get('/categoria/index_cliente')
    assert response.status_code == 200
    assert b'categoria' in response.data

def test_add_categoria(client):
    data = {
        'nombre': 'Corte de cabello',
        'descripcion': 'Diferentes estilos de corte',
    }
    imagen = (io.BytesIO(b"contenido de imagen falsa"), 'test.jpg')
    data['imagen'] = imagen
    response = client.post('/categoria/add', data=data, 
                           content_type='multipart/form-data',
                           follow_redirects=True)
    assert response.status_code == 200
    assert b'categoria' in response.data

def test_edit_categoria(client):
    categoria = Categoria(nombre='Tinte', descripcion='Coloración del cabello', imagen='tinte.jpg')
    with client.application.app_context():
        db.session.add(categoria)
        db.session.commit()
        categoria_id = categoria.idCategoria

    data = {
        'nombre': 'Tinte de cabello',
        'descripcion': 'Coloración y mechas',
        'imagen': 'nueva_tinte.jpg'
    }
    response = client.post(f'/categoria/edit/{categoria_id}', 
                           data=data,
                           content_type='multipart/form-data',
                           follow_redirects=True)
    assert response.status_code == 200
    assert b'categoria' in response.data

    # Verificar que los cambios se aplicaron correctamente
    with client.application.app_context():
        categoria_actualizada = db.session.get(Categoria, categoria_id)
        assert categoria_actualizada.nombre == 'Tinte de cabello'
        assert categoria_actualizada.descripcion == 'Coloración y mechas'

def test_delete_categoria(client):
    categoria = Categoria(nombre='Peinado', descripcion='Estilos de peinado', imagen='peinado.jpg')
    with client.application.app_context():
        db.session.add(categoria)
        db.session.commit()
        categoria_id = categoria.idCategoria

    response = client.get(f'/categoria/delete/{categoria_id}', follow_redirects=True)
    assert response.status_code == 200
    assert b'dataC' not in response.data

    # Verificar que la categoría fue eliminada
    with client.application.app_context():
        categoria_eliminada = db.session.get(Categoria, categoria_id)
        assert categoria_eliminada is None