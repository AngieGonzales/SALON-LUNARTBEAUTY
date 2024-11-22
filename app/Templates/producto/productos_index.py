import flet as ft

def main(page: ft.Page):
    page.title = "LunArt Beauty-Servicios"
    page.bgcolor = ft.colors.WHITE
    page.scroll = ft.ScrollMode.ALWAYS
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    # Header
    encabezado = ft.Container(
        content=ft.Row(
            controls=[
                ft.Text("LunArt Beauty", size=30, weight="bold", color=ft.colors.BLACK, font_family="Arizonia"),
            ],
            alignment=ft.MainAxisAlignment.START,
        ),
        bgcolor=ft.colors.GREY_300,  # Fondo gris para el encabezado
        border_radius=ft.border_radius.all(10),  # Radio de borde para el contenedor
        padding=10,  # Espaciado dentro del contenedor
    )

    # Menu Items
    menu_items = ft.Row(
        controls=[
            ft.TextButton("SERVICIOS", on_click=lambda e: None, style=ft.ButtonStyle(color=ft.colors.GREY_800)),
            ft.TextButton("CATEGORIAS", on_click=lambda e: None, style=ft.ButtonStyle(color=ft.colors.GREY_800)),
            ft.TextButton("CONTACTO", on_click=lambda e: None, style=ft.ButtonStyle(color=ft.colors.GREY_800)),
            ft.TextButton("CITAS", on_click=lambda e: None, style=ft.ButtonStyle(color=ft.colors.GREY_800)),
        ],
        alignment=ft.MainAxisAlignment.CENTER,  # Centrar los botones en la fila
        spacing=20,  # Espaciado entre botones
    )

    # Main Layout
    page.add(
        encabezado,
        menu_items,
    )

ft.app(target=main)
