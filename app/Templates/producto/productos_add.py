import flet as ft

def main(page: ft.Page):
    page.title = "LunArtBeauty - Servicios Administrador"
    page.bgcolor = ft.colors.WHITE
    page.scroll = ft.ScrollMode.ALWAYS
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Sidebar
    sidebar = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("LunArtBeauty", size=36, weight="bold", color=ft.colors.BLACK, font_family="Arizonia"),
                ft.Container(
                    content=ft.Image(
                        src="app/Imagenes/maquillaje.png",
                        width=100,
                        height=100,
                        fit=ft.ImageFit.COVER,
                    ),
                    alignment=ft.alignment.center,
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

    content = ft.Container(
        content=ft.Column(
            controls=[
                ft.Container(
                    content=ft.Text("AGREGAR PRODUCTOS", size=28, weight="bold", font_family="Times New Roman"),
                    alignment=ft.alignment.center,  # Centra el título
                    padding=ft.padding.symmetric(vertical=20),
                ),
                ft.Row(
                    controls=[
                        ft.TextField(label="Nombre", width=400),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    controls=[
                        ft.TextField(label="URL de la imagen", width=400),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    controls=[
                        ft.TextField(label="Precio", width=400),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    controls=[
                        ft.TextField(label="Categoria", width=400),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    controls=[
                        ft.TextField(label="Stock", width=400),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Container(
                    content=ft.ElevatedButton(
                        text="AGREGAR",
                        on_click=lambda e: print("Servicio agregado"),
                        icon=ft.icons.ADD, color=ft.colors.PINK,
                        bgcolor=ft.colors.GREY_300,
                    ),
                    alignment=ft.alignment.center,  # Centra el botón
                    padding=ft.padding.symmetric(vertical=20),
                ),
            ],
            spacing=20,
        ),
        expand=True,
        alignment=ft.alignment.center,  # Centra todo el formulario
    )

    # Main Layout
    page.add(
        ft.Row(
            controls=[
                sidebar,
                content,
            ],
            expand=True,
        )
    )

ft.app(target=main)
