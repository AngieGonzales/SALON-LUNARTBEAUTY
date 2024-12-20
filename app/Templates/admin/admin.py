import flet as ft


def main(page: ft.Page):
    page.title = "LunArt Beauty - Admin Panel"
    page.bgcolor = ft.colors.WHITE
    page.scroll = ft.ScrollMode.ALWAYS

    # Sidebar
    sidebar = ft.Container(
        width=250,
        bgcolor=ft.colors.GREY_300,
        content=ft.Column(
            [
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text("LunArt Beauty", size=24, weight="bold"),
                            ft.Image(src="path/to/estilistaa.png", width=100, height=100),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=10,
                    ),
                    padding=10,
                    alignment=ft.alignment.center,
                ),
                ft.ListView(
                    expand=True,
                    controls=[
                        ft.ListTile(
                            leading=ft.Image(src="path/to/tijeras.png", width=30, height=30),
                            title=ft.Text("ESTILISTAS"),
                            on_click=lambda _: print("Ir a Estilistas"),
                        ),
                        ft.ListTile(
                            leading=ft.Image(src="path/to/orden.png", width=30, height=30),
                            title=ft.Text("CATEGORÍAS"),
                            on_click=lambda _: print("Ir a Categorías"),
                        ),
                        ft.ListTile(
                            leading=ft.Image(src="path/to/campana.png", width=30, height=30),
                            title=ft.Text("PRODUCTOS"),
                            on_click=lambda _: print("Ir a Productos"),
                        ),
                        ft.ListTile(
                            leading=ft.Image(src="path/to/calendario.png", width=30, height=30),
                            title=ft.Text("CITAS"),
                            on_click=lambda _: print("Ir a Citas"),
                        ),
                        ft.ListTile(
                            leading=ft.Image(src="path/to/servicio.png", width=30, height=30),
                            title=ft.Text("SERVICIOS"),
                            on_click=lambda _: print("Ir a Servicios"),
                        ),
                        ft.ListTile(
                            leading=ft.Image(src="path/to/personas.png", width=30, height=30),
                            title=ft.Text("CLIENTES"),
                            on_click=lambda _: print("Ir a Clientes"),
                        ),
                    ],
                ),
            ],
            spacing=20,
            alignment=ft.MainAxisAlignment.START,
        ),
    )

    # Main content
    admin_info = ft.Container(
        expand=True,
        content=ft.Column(
            [
                ft.Text("ADMINISTRADOR - LUNART BEAUTY", size=28, weight="bold", color=ft.colors.GREY_800),
                ft.Container(
                    content=ft.Text(
                        "¡Bienvenido al panel de control de LunArt Beauty!\n\n"
                        "Gestiona eficientemente todos los aspectos de tu salón de belleza: productos, servicios, citas y clientes.\n\n"
                        "¡Que tengas un excelente día!",
                        size=16,
                        color=ft.colors.GREY_600,
                    ),
                    padding=20,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        ),
    )

    # Layout
    page.add(
        ft.Row(
            [sidebar, admin_info],
            expand=True,
            spacing=0,
        )
    )


ft.app(target=main)
