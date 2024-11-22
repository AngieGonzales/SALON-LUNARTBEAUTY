import flet as ft
from flet import Page

def main(page: ft.Page):
    page.title = "LunArt Beauty - Editar Usuario"
    page.bgcolor = ft.colors.WHITE
    page.scroll = ft.ScrollMode.ALWAYS
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    encabezado = ft.Container(
        content=ft.Row(
            controls=[
                ft.Text("LunArtBeauty", size=30, weight="bold", color=ft.colors.BLACK, font_family="Arizonia"),
            ],
            alignment=ft.MainAxisAlignment.START,
        ),
        bgcolor=ft.colors.GREY_300,  # Fondo gris para el encabezado
        border_radius=ft.border_radius.all(10),  # Radio de borde para el contenedor
        padding=10,  # Espaciado dentro del contenedor
    )

    # Datos predeterminados (estos podrían ser extraídos de una base de datos)
    nombre_usuario = "Juan"
    apellido_usuario = "Pérez"
    celular_usuario = "123456789"
    correo_usuario = "juan.perez@ejemplo.com"
    fecha_nacimiento_usuario = "01/01/1990"
    rol_usuario = "Usuario"  # Este podría ser "Usuario" o "Administrador"

    campo_nombre = ft.TextField(label="Nombre", width=500, value=nombre_usuario)
    campo_apellido = ft.TextField(label="Apellido", width=500, value=apellido_usuario)
    campo_celular = ft.TextField(label="Celular", width=500, value=celular_usuario)
    campo_correo = ft.TextField(label="Correo Electrónico", width=500, value=correo_usuario)
    campo_password = ft.TextField(label="Contraseña", password=True, can_reveal_password=True, width=500)
    campo_fecha_nacimiento = ft.TextField(label="Fecha de Nacimiento (dd/mm/yyyy)", width=500, value=fecha_nacimiento_usuario)
    
    campo_rol = ft.Dropdown(
        label="Rol", width=500,
        value=rol_usuario,  # Establecemos el valor seleccionado del Dropdown
        options=[
            ft.dropdown.Option("Usuario"),
            ft.dropdown.Option("Administrador"),
        ],
    )

    boton_guardar = ft.ElevatedButton(text="GUARDAR CAMBIOS", color=ft.colors.PINK, bgcolor=ft.colors.GREY_300)

    page.add(
        ft.Column(
            [
                encabezado,
                ft.Text("EDITAR USUARIO", size=24, weight="bold", font_family= "Times New Roman", color=ft.colors.GREY_900),
                campo_nombre,
                campo_apellido,
                campo_celular,
                campo_correo,
                campo_password,
                campo_fecha_nacimiento,
                campo_rol,
                boton_guardar,
            ],
            alignment=ft.MainAxisAlignment.CENTER, 
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

ft.app(target=main)
