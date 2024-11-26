import flet as ft


def main(page: ft.Page):
    page.title = "Agregar Categorías - LunArt Beauty"
    page.scroll = ft.ScrollMode.ALWAYS
    page.bgcolor = ft.colors.WHITE

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
                            ft.Image(src="path/to/editar.png", width=100, height=100),
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
                            title=ft.Text("LISTA CLIENTES"),
                            on_click=lambda _: print("Ir a Lista Clientes"),
                        ),
                    ],
                ),
            ],
            spacing=20,
            alignment=ft.MainAxisAlignment.START,
        ),
    )

    # Formulario para agregar categorías
    def agregar_categoria(e):
        nombre = campo_nombre.value
        descripcion = campo_descripcion.value
        imagen = campo_imagen.src

        if not nombre or not descripcion or not imagen:
            page.snack_bar = ft.SnackBar(ft.Text("Todos los campos son obligatorios."))
            page.snack_bar.open = True
            page.update()
        else:
            print(f"Categoría agregada: {nombre}, {descripcion}, {imagen}")
            # Aquí puedes añadir la lógica para guardar los datos

    campo_nombre = ft.TextField(label="Nombre", width=400)
    campo_descripcion = ft.TextField(label="Descripción", width=400)
    campo_imagen = ft.FilePicker(on_result=lambda e: print(e.files[0].name))

    boton_filepicker = ft.ElevatedButton(
        text="Subir Imagen",
        on_click=lambda _: page.dialog.show_picker(campo_imagen),
    )

    boton_agregar = ft.ElevatedButton(
        text="AGREGAR",
        bgcolor=ft.colors.GREEN,
        color=ft.colors.WHITE,
        on_click=agregar_categoria,
    )

    form_content = ft.Column(
        [
            ft.Text("AGREGAR CATEGORÍAS", size=24, weight="bold"),
            campo_nombre,
            campo_descripcion,
            ft.Row([boton_filepicker, ft.Text("Selecciona una imagen...", size=12)]),
            boton_agregar,
        ],
        spacing=20,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    # Layout principal
    page.add(
        ft.Row(
            [sidebar, ft.Container(expand=True, content=form_content, padding=20)],
            expand=True,
            spacing=0,
        )
    )


ft.app(target=main)
