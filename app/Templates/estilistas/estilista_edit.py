import flet as ft
from flet import Page

def main(page: ft.Page):
    page.title = "LunArt Beauty - Editar Estilista"
    page.bgcolor = ft.colors.WHITE
    page.scroll = ft.ScrollMode.ALWAYS
    page.vertical_alignment = ft.MainAxisAlignment.START

    # Encabezado con fondo suave y bordes redondeados
    encabezado = ft.Container(
        content=ft.Row(
            controls=[
                ft.Text(
                    "LunArt Beauty",
                    size=30,
                    weight="bold",
                    color=ft.colors.BLACK,
                    font_family="Arizonia",  # Elegante tipo de letra
                ),
            ],
            alignment=ft.MainAxisAlignment.START,
        ),
        bgcolor=ft.colors.GREY_300,  # Fondo suave gris
        border_radius=ft.border_radius.all(15),  # Bordes más redondeados
        padding=20,
    )

    # Título principal con un toque de elegancia
    titulo = ft.Container(
        content=ft.Text(
            "EDITAR ESTILISTA",
            size=24,
            weight="bold",
            color=ft.colors.GREY_900,
            text_align="center",
            font_family="Times New Roman",  # Elegante tipo de letra
        ),
        padding=20,  # Espaciado para separarlo del encabezado
    )

    # Campos del formulario con bordes redondeados y fondo suave
    campo_nombre = ft.TextField(
        label="Nombre", 
        width=500, 
        border_radius=ft.border_radius.all(10), 
        bgcolor=ft.colors.GREY_100
    )
    campo_apellido = ft.TextField(
        label="Apellido", 
        width=500, 
        border_radius=ft.border_radius.all(10), 
        bgcolor=ft.colors.GREY_100
    )
    campo_telefono = ft.TextField(
        label="Teléfono", 
        width=500, 
        border_radius=ft.border_radius.all(10), 
        bgcolor=ft.colors.GREY_100
    )
 
    # Botón de guardar con bordes redondeados y cambio de color en hover
    boton_guardar = ft.ElevatedButton(
        text="GUARDAR CAMBIOS",
        color=ft.colors.PINK,
        bgcolor=ft.colors.GREY_300,
        on_hover=lambda e: e.control.update(bgcolor=ft.colors.PINK_500)  # Cambia el color en hover
    )

    # Contenedor principal con mayor separación y estilo elegante
    page.add(
        ft.Column(
            [
                encabezado,
                titulo,
                campo_nombre,
                campo_apellido,
                campo_telefono,
                boton_guardar
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=30,  # Mayor separación entre los elementos
        )
    )

ft.app(target=main)
