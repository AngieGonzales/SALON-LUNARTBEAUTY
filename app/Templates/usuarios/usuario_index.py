import flet as ft

def main(page: ft.Page):
    page.title = "LunArtBeauty - Srevicios Administrador"
    page.bgcolor = ft.colors.WHITE
    page.scroll = ft.ScrollMode.ALWAYS
    page.vertical_alignment = ft.MainAxisAlignment.START
    
    # Sidebar contenido
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
                            ft.TextButton("INICIO", icon=ft.icons.HOUSE, icon_color=ft.colors.GREY_800, style=ft.ButtonStyle(color=ft.colors.GREY_800)), padding=ft.padding.all(10)),
                        ft.Container(
                            ft.TextButton("ACTUALIZAR PERFIL", icon=ft.icons.UPDATE, icon_color=ft.colors.GREY_800, style=ft.ButtonStyle(color=ft.colors.GREY_800)), padding=ft.padding.all(10)),
                        ft.Container(
                            ft.TextButton("CERRAR SESION", icon=ft.icons.CLOSE, icon_color=ft.colors.GREY_800, style=ft.ButtonStyle(color=ft.colors.GREY_800)), padding=ft.padding.all(10)),
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
