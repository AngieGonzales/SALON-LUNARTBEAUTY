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
            ft.TextButton("CATALOGOS", on_click=lambda e: None, style=ft.ButtonStyle(color=ft.colors.GREY_800)),
            ft.TextButton("CONTACTO", on_click=lambda e: None, style=ft.ButtonStyle(color=ft.colors.GREY_800)),
            ft.TextButton("CITAS", on_click=lambda e: None, style=ft.ButtonStyle(color=ft.colors.GREY_800)),
            ft.TextButton("PERFIL", on_click=lambda e: None, style=ft.ButtonStyle(color=ft.colors.GREY_800)),
        ],
        alignment=ft.MainAxisAlignment.CENTER,  # Centrar los botones en la fila
        spacing=20,  # Espaciado entre botones
    )

    # Header Content
    header_content = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("SERVICIOS", size=24, weight="bold", text_align="center"),
            ],
            alignment="center",
        ),
        padding=20,
        alignment=ft.alignment.center,
    )

    # Agregar componentes al `Page`
    page.add(encabezado, menu_items, header_content)

def toggle_menu():
    print("Toggle menu clicked!")

ft.app(target=main)
