import flet as ft
from Models.
import requests

def main(page: ft.Page):
    page.title = "Registro de Usuarios"
    page.scroll = "adaptive"

    # Función para enviar datos al backend
    def registrar_usuario(page):
        usuario = {
            "nombre": campo_nombre.value,
            "apellido": campo_apellido.value,
            "celular": campo_celular.value,
            "correo": campo_correo.value,
            "password_hash": campo_password.value,
            "fecha_nacimiento": campo_fecha_nacimiento.value,
            "rol": campo_rol.value
        }

        # Enviar datos al endpoint
        respuesta = requests.post("http://127.0.0.1:5000/api/registro", json=usuario)
        if respuesta.status_code == 201:
            page.snack_bar = ft.SnackBar(ft.Text("Usuario registrado con éxito!"), bgcolor="green")
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Error al registrar usuario."), bgcolor="red")
        page.snack_bar.open()
        page.update()

    # Campos del formulario
    campo_nombre = ft.TextField(label="Nombre", required=True)
    campo_apellido = ft.TextField(label="Apellido", required=True)
    campo_celular = ft.TextField(label="Celular", required=True)
    campo_correo = ft.TextField(label="Correo Electrónico", required=True)
    campo_password = ft.TextField(label="Contraseña", password=True, can_reveal_password=True, required=True)
    campo_fecha_nacimiento = ft.TextField(label="Fecha de Nacimiento (dd/mm/yyyy)", required=True)
    campo_rol = ft.Dropdown(
        label="Rol",
        options=[
            ft.dropdown.Option("Usuario"),
            ft.dropdown.Option("Administrador"),
        ],
        required=True
    )

    # Botón de envío
    boton_registrar = ft.ElevatedButton(text="Registrar", on_click=registrar_usuario)

    # Agregar todos los elementos a la página
    page.add(
        ft.Text("Formulario de Registro", size=24, weight="bold"),
        campo_nombre,
        campo_apellido,
        campo_celular,
        campo_correo,
        campo_password,
        campo_fecha_nacimiento,
        campo_rol,
        boton_registrar
    )

ft.app(target=main)
