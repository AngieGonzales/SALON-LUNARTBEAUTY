import flet as ft

def main(page: ft.Page):
    # Configuración de la página
    page.title = "Perfil de Usuario - LunArt Beauty"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0
    page.bgcolor = "white"
    
    # Sidebar contenido
    sidebar = ft.Container(
        content=ft.Column(
            controls=[
                ft.Container(
                    content=ft.Text("LunArt Beauty", size=20, weight=ft.FontWeight.BOLD),
                    alignment=ft.alignment.center,
                ),
                ft.ListView(
                    controls=[
                        ft.ListTile(
                            leading=ft.Image(src="/static/img/casa.png", width=30, height=30),
                            title=ft.Row(
                                controls=[
                                    ft.Image(src="/static/img/home_icon.png", width=20, height=20),
                                    ft.Text("INICIO", expand=True),
                                ],
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            ),
                            on_click=lambda e: page.go("/menu/ruta_inicio"),
                        ),
                        ft.ListTile(
                            leading=ft.Image(src="/static/img/personas.png", width=30, height=30),
                            title=ft.Row(
                                controls=[
                                    ft.Image(src="/static/img/update_profile.png", width=20, height=20),
                                    ft.Text("ACTUALIZAR PERFIL", expand=True),
                                ],
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            ),
                            on_click=lambda e: page.go("/usuario/lista_usuarios"),
                        ),
                        ft.ListTile(
                            leading=ft.Image(src="/static/img/tijeras.png", width=30, height=30),
                            title=ft.Row(
                                controls=[
                                    ft.Image(src="/static/img/stylists.png", width=20, height=20),
                                    ft.Text("ESTILISTAS", expand=True),
                                ],
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            ),
                            on_click=lambda e: page.go("/estilistas/index"),
                        ),
                        ft.ListTile(
                            leading=ft.Image(src="/static/img/cerrar.png", width=30, height=30),
                            title=ft.Row(
                                controls=[
                                    ft.Image(src="/static/img/logout.png", width=20, height=20),
                                    ft.Text("CERRAR SESIÓN", expand=True),
                                ],
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            ),
                            on_click=lambda e: page.go("/usuario/logout"),
                        ),
                    ]
                )
            ],
            expand=True,
        ),
        width=250,
        bgcolor="#f0f0f0",
        padding=10,
    )

    # Contenido principal
    content = ft.Column(
        controls=[
            ft.Text("Bienvenido a tu Perfil", size=24, weight=ft.FontWeight.BOLD),
            ft.Text("Aquí puedes encontrar información y opciones para gestionar tu perfil."),
            # Nueva imagen añadida aquí
            ft.Image(src="app/Imagenes/logo.png", width=1000, height=300, fit=ft.ImageFit.CONTAIN),
        ],
        expand=True,
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    # Estructura principal
    main_container = ft.Row(
        controls=[
            sidebar,
            ft.Container(
                content=ft.Column(
                    controls=[content],
                ),
                expand=True,
                bgcolor="white",
                padding=20,
            )
        ],
        expand=True,
    )

    page.add(main_container)

ft.app(target=main, assets_dir="static")
