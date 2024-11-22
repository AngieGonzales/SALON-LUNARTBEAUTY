import flet as ft

def main(page: ft.Page):
    page.title = "Login - LunArt Beauty"
    
    # Centrar contenido en toda la página
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Función para manejar el botón de inicio de sesión
    def iniciar_sesion(e):
        correo = correo_input.value
        contrasena = contrasena_input.value
        if correo and contrasena:
            ft.dialog(
                title="Inicio de Sesión",
                content=f"Bienvenido, {correo}!",
                actions=[ft.TextButton("Cerrar", on_click=lambda e: page.close_dialog())],
            ).show(page)
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Por favor completa todos los campos."), duration=2000)
            page.snack_bar.open()

    # Título del login
    login_title = ft.Container(
        content=ft.Text(
            "LOGIN",
            weight=ft.FontWeight.BOLD,
            text_align=ft.TextAlign.CENTER,  
            font_family="Times New Roman",
            size=28,  
        ),
        alignment=ft.alignment.center,  
    )

    # Campo de entrada para correo
    correo_input = ft.TextField(
        label="Correo",
        icon=ft.icons.EMAIL,
        width=350,
    )

    # Campo de entrada para contraseña
    contrasena_input = ft.TextField(
        label="Contraseña",
        icon=ft.icons.LOCK,
        password=True,
        can_reveal_password=True,
        width=350,
    )

    # Botón para iniciar sesión
    iniciar_sesion_btn = ft.ElevatedButton(
        text="Iniciar sesión",
        color=ft.colors.WHITE,
        bgcolor=ft.colors.PINK_300,
        width=200,
        on_click=iniciar_sesion,
    )

    # Botón de registrarse: Cambia de vista a la página de registro
    def ir_a_registro(e):
        page.go("/registro")  # Cambié "registro/register" a "/registro"

    registrarse_btn = ft.TextButton(
        text="Registrarse",
        on_click=ir_a_registro,
    )

    # Contenedores para mover los campos
    correo_input_container = ft.Container(
        content=correo_input,
        alignment=ft.alignment.Alignment(0.0, 0.0),  
        width=500,
    )

    contrasena_input_container = ft.Container(
        content=contrasena_input,
        alignment=ft.alignment.Alignment(0.0, 0.0),  
        width=500,
    )

    # Construcción del formulario
    login_form = ft.Container(
        content=ft.Column(
            [
                login_title,  
                correo_input_container,  
                contrasena_input_container,  
                ft.Container(content=iniciar_sesion_btn, alignment=ft.alignment.center),
                ft.Container(content=registrarse_btn, alignment=ft.alignment.center),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,  
        ),
        width=500,
        height=400,  
        border_radius=20,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right,
            colors=[ft.colors.WHITE, ft.colors.PINK_100],
        ),
        shadow=ft.BoxShadow(color=ft.colors.BLACK12, blur_radius=15, spread_radius=5),
        alignment=ft.alignment.center,  
    )

    # Añadir formulario a la página
    page.add(login_form)

ft.app(target=main)
