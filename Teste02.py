import flet as ft

def main(page: ft.Page):
    page.bgcolor = "#121212"  # Fundo escuro
    page.window_maximized = True  # Iniciar maximizado
    page.window_resizable = True  # Permitir redimensionamento

    # Container que expande para todos os lados
    main_container = ft.Container(
        expand=True,
        bgcolor="blue",  # Cor de fundo do container
        border_radius=15,  # Borda arredondada
        content=ft.Text("Container Expandido", size=20, color="white", weight="bold"),
        alignment=ft.alignment.center,  # Centraliza o texto dentro do container
    )

    # Adiciona o container à tela
    page.add(main_container)

ft.app(target=main)
