import flet as ft
from flet import Page


def main (page: ft.Page):
    page.title = "Registro de Usuarios"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.padding = 0

    encabezado = ft.Container(
        content=ft.Text(
            "LunartBeauty",
            size=30,
            weight="bold",
            color=ft.colors.BLACK,
            font_family= "Arizonia"
        ),
        padding=10,
        bgcolor=ft.colors.GREY_200,
        alignment=ft.alignment.top_left,
        border_radius=ft.border_radius.all(10),
        width= None,
    )

    def registrar_usuario():
        usuario = {
                "nombre": campo_nombre.value,
                "apellido": campo_apellido.value,
                "celular": campo_celular.value,
                "correo": campo_correo.value,
                "password_hash": campo_password.value,
                "fecha_nacimiento": campo_fecha_nacimiento.value,
                "rol": campo_rol.value
            }


    campo_nombre = ft.TextField(label="Nombre", width=500)
    campo_apellido = ft.TextField(label="Apellido", width=500,)
    campo_celular = ft.TextField(label="Celular", width=500,)
    campo_correo = ft.TextField(label="Correo Electrónico", width=500,)
    campo_password = ft.TextField(label="Contraseña", password=True, can_reveal_password=True, width=500,)
    campo_fecha_nacimiento = ft.TextField(label="Fecha de Nacimiento (dd/mm/yyyy)", width=500,)
    campo_rol = ft.Dropdown(
        label="Rol", width=500,
        options=[
            ft.dropdown.Option("Usuario"),
            ft.dropdown.Option("Administrador"),
        ],
    )

    boton_registrar = ft.ElevatedButton(text="REGISTRAR", color= ft.colors.PINK_500, bgcolor=ft.colors.GREY_300, on_click=registrar_usuario)

    page.add(
        ft.Column(
            [
                encabezado,
                ft.Text("FORMULARIO DE REGISTRO", size=24, weight="bold", color=ft.colors.GREY_900),
                campo_nombre,
                campo_apellido,
                campo_celular,
                campo_correo,
                campo_password,
                campo_fecha_nacimiento,
                campo_rol,
                boton_registrar,
            ],
            alignment=ft.MainAxisAlignment.CENTER, 
            horizontal_alignment=ft.CrossAxisAlignment.CENTER, 
        )
    )

ft.app(target=main)