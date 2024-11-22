import flet as ft

def main(page: ft.Page):
    page.title = "LunArt Beauty - Menú"
    page.bgcolor = ft.colors.WHITE
    page.scroll = ft.ScrollMode.ALWAYS

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
        bgcolor=ft.colors.GREY_300, # Fondo suave rosado
        border_radius=ft.border_radius.all(15),  # Bordes más redondeados
        padding=20,
       
    )

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

    # Header Content Section
    header_content = ft.Container(
        content=ft.Row(
            controls=[
                ft.Image(
                    src="app/static/img/20.png",
                    width=500,
                    height=500,
                    fit=ft.ImageFit.CONTAIN,
                ),
                ft.Column(
                    controls=[
                        ft.Text(
                            "TU BELLEZA, NUESTRO COMPROMISO",
                            size=32,
                            weight="bold",
                            color=ft.colors.PINK,
                        ),
                        ft.Text(
                            '"Descubre lo mejor de nuestros servicios y productos."',
                            size=18,
                            italic=True,
                            color=ft.colors.GREY_600,
                        ),
                        ft.ElevatedButton(
                            "INFORMACION",
                            on_click=lambda e: print("Ir a Información"),
                            style=ft.ButtonStyle(
                                bgcolor=ft.colors.PINK,
                                color=ft.colors.WHITE,
                                padding=ft.padding.symmetric(horizontal=20, vertical=10),
                                shape=ft.RoundedRectangleBorder(radius=10),
                            ),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=20,
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
        ),
        padding=20,
    )

    # Add components to page
    page.add(
        encabezado,
        menu_items,
        header_content,
    )

ft.app(target=main)
