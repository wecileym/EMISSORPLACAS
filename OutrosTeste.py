import flet as ft

class SettingsScreen(ft.UserControl):
    def __init__(self):
        super().__init__()
        
        # Contêiner para o conteúdo dinâmico
        self.content_container = ft.Container(
            content=ft.Column(expand=True),  # Expande internamente
            padding=20,
            bgcolor=ft.colors.GREY_400,
            border_radius=15,
            shadow=ft.BoxShadow(blur_radius=10, color=ft.colors.BLACK12),
            expand=True,  # Expande externamente
        )

    def show_perfil(self):
        # Atualiza o conteúdo dentro do contêiner
        self.content_container.content.controls = [
            ft.Text("Perfil do Usuário", style=ft.TextStyle(weight=ft.FontWeight.BOLD, size=20)),
            ft.ElevatedButton("Editar Perfil", icon=ft.icons.EDIT),
            ft.ElevatedButton("Voltar", icon=ft.icons.ARROW_BACK),
        ]
        self.content_container.content.update()  # Atualiza o layout interno
        self.update()  # Atualiza toda a interface

    def build(self):
        # Criando a barra de menu
        menu_bar = ft.MenuBar(
            expand=True,  # Expande horizontalmente
            style=ft.MenuStyle(
                alignment=ft.alignment.top_left,
                bgcolor=ft.colors.GREY_500,
                mouse_cursor={
                    ft.ControlState.HOVERED: ft.MouseCursor.WAIT,
                    ft.ControlState.DEFAULT: ft.MouseCursor.ZOOM_OUT,
                },
            ),
            controls=[
                ft.SubmenuButton(
                    content=ft.Text("Configurações"),
                    controls=[
                        ft.MenuItemButton(
                            content=ft.Text("Perfil"),
                            leading=ft.Icon(ft.icons.PERSON_OFF_OUTLINED),
                            style=ft.ButtonStyle(bgcolor={ft.ControlState.HOVERED: ft.colors.GREEN_100}),
                            on_click=lambda _: self.show_perfil(),
                        ),
                    ],
                ),
            ],
        )

        # Criando a estrutura da tela com ambos expandindo
        return ft.Column(
            controls=[
                menu_bar,  # Barra de menu que se expande
                ft.Container(
                    content=self.content_container,
                    expand=True,  # Expande o container para ocupar o espaço disponível
                ),
            ],
            expand=True  # Expande toda a coluna para preencher a tela
        )

def main(page: ft.Page):
    page.add(SettingsScreen())

ft.app(target=main)
