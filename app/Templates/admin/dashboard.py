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

    # Admin Info Section
    admin_info = ft.Container(
        content=ft.Column(
            controls=[
                ft.Container(
                    content=ft.Text(
                        "ADMINISTRADOR - LUNART BEAUTY",
                        size=24,
                        weight="bold",
                        color=ft.colors.PINK,
                        font_family="Times New Roman"
                    ),
                    alignment=ft.alignment.center,
                    padding=20,
                ),
                ft.Container(
                    content=ft.Text(
                        "Bienvenidos",
                        size=20,
                        weight="bold",
                        color=ft.colors.GREY_700,
                    ),
                    padding=ft.padding.symmetric(vertical=10),
                    alignment=ft.alignment.center
                ),
                ft.Container(
                    content=ft.Text(
                        (
                            "¡Nos alegra verte de nuevo en el panel de control de LunArt Beauty! Aquí podrás gestionar "
                            "de manera eficiente todos los aspectos de tu salón de belleza. Desde la administración de "
                            "productos y servicios hasta la gestión de citas y clientes, este panel te proporciona todas "
                            "las herramientas necesarias para mantener el negocio en funcionamiento y ofrecer la mejor "
                            "experiencia a tus clientes.\n\n"
                            "No olvides revisar las últimas notificaciones y estar al tanto de las actualizaciones importantes. "
                            "Si necesitas asistencia, no dudes en consultarnos en la sección de ayuda.\n\n"
                            "¡Que tengas un excelente día de trabajo!"
                        ),
                        size=16,
                        text_align="justify",
                        color=ft.colors.GREY_800,
                    ),
                    padding=20,
                ),
            ],
            alignment=ft.MainAxisAlignment.START,
            spacing=20,
        ),
        expand=True,
        padding=20,
    )

    # Main Layout
    page.add(
        ft.Row(
            controls=[
                sidebar,
                admin_info,
            ],
            expand=True,
        )
    )

ft.app(target=main)
