import flet as ft

def main(page: ft.Page):
    page.title = "LunArt Beauty - Lista de Clientes"
    page.bgcolor = ft.colors.WHITE
    page.scroll = ft.ScrollMode.ALWAYS
    page.vertical_alignment = ft.MainAxisAlignment.START

    # Sidebar
    sidebar = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("LunArtBeauty", size=36, weight="bold", color=ft.colors.BLACK, font_family="Times New Roman"),
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

    # Tabla de Clientes
    table = ft.Column(
        controls=[
            ft.Row(
                controls=[
                    ft.Text("ID", weight="bold", color=ft.colors.GREY_800),
                    ft.Text("Nombre", weight="bold", color=ft.colors.GREY_800),
                    ft.Text("Apellido", weight="bold", color=ft.colors.GREY_800),
                    ft.Text("Celular", weight="bold", color=ft.colors.GREY_800),
                    ft.Text("Correo", weight="bold", color=ft.colors.GREY_800),
                    ft.Text("Fecha de Nacimiento", weight="bold", color=ft.colors.GREY_800),
                    ft.Text("Acciones", weight="bold", color=ft.colors.GREY_800),
                ],
                alignment=ft.MainAxisAlignment.START,
                spacing=20,
                height=40,
            ),
        ],
        spacing=10,
    )

    # Supongamos que 'data' es una lista de objetos de cliente
    data = [
        {"id": 1, "nombre": "Juan", "apellido": "Pérez", "celular": "123456789", "correo": "juan@mail.com", "fecha_nacimiento": "1990-01-01"},
        {"id": 2, "nombre": "María", "apellido": "Gómez", "celular": "987654321", "correo": "maria@mail.com", "fecha_nacimiento": "1992-02-02"},
        # Más datos de clientes...
    ]

    # Agregar los clientes a la tabla
    for usuario in data:
        table.controls.append(
            ft.Row(
                controls=[
                    ft.Text(str(usuario["id"])),
                    ft.Text(usuario["nombre"]),
                    ft.Text(usuario["apellido"]),
                    ft.Text(usuario["celular"]),
                    ft.Text(usuario["correo"]),
                    ft.Text(usuario["fecha_nacimiento"]),
                    ft.Row(
                        controls=[
                            ft.IconButton(ft.icons.EDIT, on_click=lambda e, user_id=usuario["id"]: print(f"Editar {user_id}")),
                            ft.IconButton(ft.icons.DELETE, on_click=lambda e, user_id=usuario["id"]: print(f"Eliminar {user_id}"))
                        ],
                        spacing=10,
                    ),
                ],
                spacing=20,
                alignment=ft.MainAxisAlignment.START,
                height=40,
            )
        )

    # Contenedor principal
    page.add(
    ft.Row(
        controls=[
            sidebar,
            ft.Column(
                controls=[
                    ft.Container(
                        content=ft.Text(
                            "Lista de Clientes",
                            size=24,
                            weight="bold",
                            color=ft.colors.GREY_800,
                            font_family="Times New Roman",
                        ),
                        padding=20,
                        alignment=ft.alignment.center,  # Centra el texto
                        width=800,  # Asegúrate de que coincida con la tabla
                    ),
                    ft.Container(
                        content=table,
                        bgcolor=ft.colors.GREY_100,
                        padding=20,
                        border_radius=10,
                        width=800,
                        height=400,
                        alignment=ft.alignment.center,  # Centra la tabla
                    ),
                ],
                width=page.width - 250,
                alignment=ft.MainAxisAlignment.CENTER,  # Centra la columna que contiene la tabla
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,  # Centra toda la fila
        spacing=20,
    )
)



ft.app(target=main)
