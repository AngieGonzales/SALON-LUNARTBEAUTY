import flet as ft

def main(page: ft.Page):
    page.title = "LunArtBeauty - Servicios Administrador"
    page.bgcolor = ft.colors.WHITE
    page.scroll = ft.ScrollMode.ALWAYS
    page.vertical_alignment = ft.MainAxisAlignment.START

    # Sidebar
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

    # Content: Form to Add Services
    content = ft.Container(
    content=ft.Column(
        controls=[
            ft.Container(
                content=ft.Text("AGREGAR SERVICIOS", size=28, weight="bold"),
                alignment=ft.alignment.center,
                padding=20
            ),
            # URL field with label aligned center
            ft.Row(
                controls=[
                    ft.Text("URL:", weight="bold", width=100, text_align="right"),  # Label
                    ft.TextField(
                        label="URL de la imagen",
                        on_change=lambda e: page.add(ft.Text(f"URL ingresada: {e.control.value}")),
                        width=400,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,  # Centra toda la fila
                spacing=10
            ),
            ft.Row(
                controls=[
                    ft.Text("Nombre:", weight="bold", width=100, text_align="right"),  # Label
                    ft.TextField(
                        label="Nombre Servicio",
                        width=400,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,  # Centra toda la fila
                spacing=20
            ),
            ft.Row(
                controls=[
                    ft.Text("Descripción:", weight="bold", width=100, text_align="right"),  # Label
                    ft.TextField(
                        label="Descripción Servicio",
                        width=400,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,  # Centra toda la fila
                spacing=10
            ),
            ft.ElevatedButton(
                text="AGREGAR",
                on_click=lambda e: page.go("/servicio.add"),
                icon=ft.icons.ADD, color=ft.colors.PINK,
                bgcolor=ft.colors.GREY_300
            ),
        ],
        spacing=20,
        alignment=ft.MainAxisAlignment.CENTER,  # Centra los controles dentro de la columna
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    ),
    expand=True,  # Ocupa todo el espacio restante
    alignment=ft.alignment.center  # Centra el formulario dentro del contenedor
)


    # Main Layout
    page.add(
        ft.Row(
            controls=[
                sidebar,
                content,
            ],
            expand=True,  # Hace que el Row ocupe todo el espacio disponible
            alignment=ft.MainAxisAlignment.CENTER,  # Centra los elementos dentro del Row
            vertical_alignment=ft.CrossAxisAlignment.CENTER  # Asegura que los elementos estén centrados verticalmente
        )
    )

ft.app(target=main)
