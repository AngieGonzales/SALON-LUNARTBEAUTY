import flet as ft

def main(page: ft.Page):
    page.title = "LunArtBeauty - Contacto"
    page.bgcolor = ft.colors.WHITE
    page.scroll = ft.ScrollMode.ALWAYS
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Encabezado
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

    # Menú
    menu_items = [
        ft.TextButton("SERVICIOS", on_click=lambda e: None, style=ft.ButtonStyle(color=ft.colors.GREY_800)),
        ft.TextButton("CATALOGOS", on_click=lambda e: None, style=ft.ButtonStyle(color=ft.colors.GREY_800)),
        ft.TextButton("CONTACTO", on_click=lambda e: None, style=ft.ButtonStyle(color=ft.colors.GREY_800)),
        ft.TextButton("CITAS", on_click=lambda e: None, style=ft.ButtonStyle(color=ft.colors.GREY_800)),
        ft.TextButton("PERFIL", on_click=lambda e: None, style=ft.ButtonStyle(color=ft.colors.GREY_800)),
    ]

    nav_menu = ft.Row(
        controls=menu_items,
        alignment=ft.MainAxisAlignment.CENTER,  # Alinea el menú en el centro
    )

    # Información de contacto
    contacto_info = ft.Column(
        controls=[
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text("Horario de atención", size=20, weight="bold", color=ft.colors.GREY_800),
                        ft.Text("Lunes - Viernes: 8am a 5pm"),
                        ft.Text("Sábado: 8am a 11am"),
                        ft.Text("Domingo: cerrado"),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                ),
                padding=10,
                bgcolor=ft.colors.GREY_200,
                border_radius=10,
            ),
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text("Contacto", size=20, weight="bold"),
                        ft.Text("Número de teléfono: +1 234 567 890"),
                        ft.Text("Email: contacto@gmail.com"),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                ),
                padding=10,
                bgcolor=ft.colors.GREY_200,
                border_radius=10,
            ),
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text("Dirección", size=20, weight="bold"),
                        ft.Text("Ubicación: 1 Stanford Street, Londres, Inglaterra"),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                ),
                padding=10,
                bgcolor=ft.colors.GREY_200,
                border_radius=10,
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,  # Alinea los controles de la columna hacia el centro
        horizontal_alignment=ft.CrossAxisAlignment.CENTER

    )

    # Formulario de contacto
    contacto_form = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("Deja aquí tu comentario", size=28, weight="bold", color=ft.colors.BLACK, text_align= ft.TextAlign.CENTER),
                ft.Container(
                    content=ft.TextField(
                        label="Deja aquí tu comentario",
                        autofocus=True,
                        multiline=True,  # Esto convierte el campo en un área de texto multilinea
                        height=150,
                    ),
                    padding=10,
                    bgcolor=ft.colors.GREY_200,
                    border_radius=10,
                    width=700
                ),
            ],
            alignment=ft.MainAxisAlignment.START,  # Alinea los controles hacia el inicio
        ),
        padding=20,  # Aplica el padding al contenedor completo
    )

    boton_registrar = ft.ElevatedButton(text="ENVIAR", color= ft.colors.PINK_500, bgcolor=ft.colors.GREY_300)

    page.add(
        ft.Column(
            controls=[encabezado, nav_menu, contacto_info, contacto_form, boton_registrar],
            alignment=ft.MainAxisAlignment.CENTER,  # Alineación vertical de los elementos dentro de la página
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

ft.app(target=main)
