import flet as ft

def main(page: ft.Page):
    page.title = "LunArtBeauty - Usuarios"
    page.bgcolor = ft.colors.WHITE
    page.scroll = ft.ScrollMode.ALWAYS
    page.vertical_alignment = ft.MainAxisAlignment.START


    sidebar = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("LunArtBeauty", size=36, weight="bold", color=ft.colors.BLACK, font_family="Arizonia"),
                ft.Container(
                    content=ft.Image(
                        src="app/Imagenes/maquillaje.png",  # Ruta de la imagen
                        width=100,
                        height=100,
                        fit=ft.ImageFit.COVER,
                    ),
                    alignment=ft.alignment.center,  # Centra la imagen dentro del contenedor
                ),
                ft.ListView(
                    expand=True,
                    controls=[
                        ft.Container(
                            ft.TextButton("ESTILISTAS", icon=ft.icons.BRUSH, icon_color=ft.colors.GREY_800, style=ft.ButtonStyle(color=ft.colors.GREY_800)), padding=ft.padding.all(10)),
                        ft.Container(
                            ft.TextButton("CATEGORIAS", icon=ft.icons.CATEGORY, icon_color=ft.colors.GREY_800, style=ft.ButtonStyle(color=ft.colors.GREY_800)), padding=ft.padding.all(10)),
                        ft.Container(
                            ft.TextButton("PRODUCTOS", icon=ft.icons.SHOPPING_BAG, icon_color=ft.colors.GREY_800, style=ft.ButtonStyle(color=ft.colors.GREY_800)), padding=ft.padding.all(10)),
                        ft.Container(
                            ft.TextButton("CITAS", icon=ft.icons.CALENDAR_TODAY, icon_color=ft.colors.GREY_800, style=ft.ButtonStyle(color=ft.colors.GREY_800)), padding=ft.padding.all(10)),
                        ft.Container(
                            ft.TextButton("SERVICIOS", icon=ft.icons.BUILD, icon_color=ft.colors.GREY_800, style=ft.ButtonStyle(color=ft.colors.GREY_800)), padding=ft.padding.all(10)),
                        ft.Container(
                            ft.TextButton("CLIENTES", icon=ft.icons.PEOPLE, icon_color=ft.colors.GREY_800, style=ft.ButtonStyle(color=ft.colors.GREY_800)), padding=ft.padding.all(10)),
                    ],
                ),
            ],
            spacing=50,
        ),
        width=280,
        height=680,
        bgcolor=ft.colors.GREY_200,
        padding=20,
    )

    content_header = ft.Container(
        content=ft.Text("LISTA DE USUARIOS", size=24, weight="bold"),
        padding=20,
        alignment=ft.alignment.center,
    )

    table_header = ft.Row(
        controls=[
            ft.Text("ID", weight="bold"),
            ft.Text("NOMBRE", weight="bold"),
            ft.Text("APELLIDO", weight="bold"),
            ft.Text("CELULAR", weight="bold"),
            ft.Text("CORREO", weight="bold"),
            ft.Text("NACIMIENTO", weight="bold"),
            ft.Text("ROL", weight="bold"),
        ],
        alignment=ft.MainAxisAlignment.SPACE_AROUND,
        height=40,
    )

    # Main Layout
    page.add(
        ft.Row(
            controls=[
                sidebar,
                ft.Container(
                    content=ft.Column(
                        controls=[
                            content_header,
                            table_header,
                        ],
                        spacing=20,
                    ),
                    expand=True,
                    padding=20,
                ),
            ],
        )
    )


ft.app(target=main)
