import flet as ft

def main(page: ft.Page):
    page.title = "LunArtBeauty - Editar Productos"
    page.bgcolor = ft.colors.WHITE
    page.scroll = ft.ScrollMode.ALWAYS
    page.vertical_alignment = ft.MainAxisAlignment.START

    selected_image = ft.Image(src=None, width=200, height=200)

    def upload_file(e):
        file_dialog.pick_files(allow_multiple=False)

    def on_file_picked(e):
        if e.files:
            # Mostrar la imagen seleccionada
            selected_image.src = e.files[0].path
            selected_image.update()
            print(f"File selected: {e.files[0].name}")
        else:
            print("No file selected")

    file_dialog = ft.FilePicker(on_result=on_file_picked)

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

    content = ft.Container(
        content=ft.Column(
            [
                ft.Text("EDITAR PRODUCTOS", size=24, weight="bold", font_family="Times New Roman"),
                ft.ElevatedButton("Seleccionar Imagen", on_click=upload_file, color=ft.colors.PINK),
                selected_image,
                ft.TextField(label="Nombre", width=500),
                ft.TextField(label="Precio", width=500),
                ft.TextField(label="Stock", width=500),
                ft.ElevatedButton("ACTUALIZAR", on_click=lambda _: print("Servicio actualizado"), color=ft.colors.PINK, icon=ft.icons.UPDATE),
            ],
            spacing=20,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Centra los elementos horizontalmente
            alignment=ft.MainAxisAlignment.CENTER,  # Centra los elementos verticalmente
        ),
        alignment=ft.alignment.center,  # Centra el contenido en relación al contenedor
        expand=True,
        padding=20,
    )

    # Main layout
    main_layout = ft.Row(
        [sidebar, content],
        expand=True,
    )

    page.overlay.append(file_dialog)
    page.add(main_layout)

ft.app(target=main)