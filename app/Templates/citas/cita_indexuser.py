import flet as ft

def main(page: ft.Page):
    page.title = "LunArt Beauty - Lista de Citas"
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
                            ft.TextButton("SERVICIOS", icon=ft.icons.BUILD, icon_color=ft.colors.GREY_800, style=ft.ButtonStyle(color=ft.colors.GREY_800)), padding=ft.padding.all(10)),
                        ft.Container(
                            ft.TextButton("CATALOGO", icon=ft.icons.CATEGORY, icon_color=ft.colors.GREY_800, style=ft.ButtonStyle(color=ft.colors.GREY_800)), padding=ft.padding.all(10)),
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

    # Lista de citas
    tabla = ft.Column(
        controls=[
            ft.Container(
                content=ft.Text("LISTA DE CITAS", size=24, weight="bold", font_family="Times New Roman", color=ft.colors.GREY_900),
                # Usa un padding para mover el texto hacia la derecha por píxeles
                padding=ft.padding.only(left=330)  # Mueve el texto 80 píxeles a la derecha
            ),
            ft.DataTable(
                columns=[
                    ft.DataColumn(ft.Text("ID")),
                    ft.DataColumn(ft.Text("FECHA")),
                    ft.DataColumn(ft.Text("HORA")),
                    ft.DataColumn(ft.Text("CLIENTE")),
                    ft.DataColumn(ft.Text("ESTILISTA")),
                    ft.DataColumn(ft.Text("SERVICIO")),
                    ft.DataColumn(ft.Text("ACCIONES")),
                ],
                rows=[
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(cita.get("idcita", "N/A"))),
                            ft.DataCell(ft.Text(cita.get("fecha", "N/A"))),
                            ft.DataCell(ft.Text(cita.get("hora", "N/A"))),
                            ft.DataCell(ft.Text(cita.get("cliente", "N/A"))),
                            ft.DataCell(ft.Text(cita.get("estilista", {}).get("nombre", "N/A"))),
                            ft.DataCell(ft.Text(cita.get("servicio", {}).get("nombre", "N/A"))),
                            ft.DataCell(
                                ft.Row(
                                    controls=[
                                        ft.IconButton(ft.icons.EDIT, on_click=lambda e, cita=cita: edit_cita(cita)),
                                        ft.IconButton(ft.icons.DELETE, on_click=lambda e, cita=cita: delete_cita(cita)),
                                    ]
                                )
                            ),
                        ]
                    ) for cita in data  # Asegúrate de tener `data` con la lista de citas
                ]
            ),
            # Botón AGENDAR centrado con icono y colores personalizados
            ft.Container(
                content=ft.ElevatedButton(
                    text="AGENDAR", 
                    icon=ft.icons.ADD, 
                    color=ft.colors.PINK, 
                    bgcolor=ft.colors.GREY_300, 
                    on_click=lambda e: page.navigate("/agendar")
                ),
                alignment=ft.alignment.center,  # Centra el botón
                padding=ft.padding.all(20),
            ),
        ],
    )

    # Estructura principal
    main_container = ft.Row(
        controls=[
            sidebar,
            ft.Container(
                content=ft.Column(
                    controls=[tabla],
                ),
                expand=True,
                bgcolor="white",
                padding=20,
            )
        ],
        expand=True,
    )

    page.add(main_container)

def toggle_menu(e):
    pass  # Implementa la lógica para mostrar u ocultar el menú si es necesario

def edit_cita(cita):
    # Lógica para editar una cita
    print(f"Editando cita: {cita.get('idcita', 'N/A')}")

def delete_cita(cita):
    # Lógica para eliminar una cita
    print(f"Eliminando cita: {cita.get('idcita', 'N/A')}")

# Asegúrate de tener una lista de citas, por ejemplo:
data = [
    {"idcita": 1, "fecha": "2024-11-01", "hora": "10:00", "cliente": "Juan Pérez", "estilista": {"nombre": "Ana"}, "servicio": {"nombre": "Corte de cabello"}},
    {"idcita": 2, "fecha": "2024-11-02", "hora": "12:00", "cliente": "Maria López", "estilista": {"nombre": "Carlos"}, "servicio": {"nombre": "Manicure"}},
]

ft.app(target=main)
