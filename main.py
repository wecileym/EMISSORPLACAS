import flet as ft

# Classes para as funcionalidades
class Screen(ft.UserControl):
    def build(self):
        return ft.Text("Tela Base - Substitua em subclasses")

class EditScreen(Screen):
    def build(self):
        return ft.Text("Tela de Edição", size=20)

class ViewScreen(Screen):
    def build(self):
        return ft.Text("Tela de Visualização", size=20)

class DownloadScreen(Screen):
    def build(self):
        return ft.Text("Tela de Downloads", size=20)

class ChartScreen(Screen):
    def build(self):
        return ft.Text("Tela de Gráficos", size=20)
class SettingsScreen(Screen):
    def build(self):
        return ft.Text("Tela de Configuração", size=20)

# Função principal
def main(page: ft.Page):

    # Função para alterar a tela exibida
    def update_content(index):
        screens = [
            EditScreen(),
            ViewScreen(),
            DownloadScreen(),
            ChartScreen(),
            SettingsScreen(),
        ]
        main_content.controls.clear()
        main_content.controls.append(screens[index])
        page.update()

    # Barra de navegação
    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=400,
        group_alignment=0.0,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.Icon(ft.Icons.CREATE_NEW_FOLDER, size=40),
                label="EDITAR",
            ),
            ft.NavigationRailDestination(
                icon=ft.Icon(ft.Icons.VISIBILITY, size=40),
                label="VISUALIZAÇÃO",
            ),
            ft.NavigationRailDestination(
                icon=ft.Icon(ft.Icons.DOWNLOAD, size=40),
                label="DOWNLOADS",
            ),
            ft.NavigationRailDestination(
                icon=ft.Icon(ft.Icons.SHOW_CHART, size=40),
                label="GRÁFICOS",
            ),
            ft.NavigationRailDestination(
                icon=ft.Icon(ft.Icons.SETTINGS, size=40),
                label="CONFIGURAÇÃO",
            ),
        ],
        on_change=lambda e: update_content(e.control.selected_index),
    )

    # Contêiner principal para exibir as telas
    main_content = ft.Column(expand=True)

    # Layout principal com a barra de navegação e o conteúdo dinâmico
    page.add(
        ft.Row(
            [
                rail,
                ft.VerticalDivider(width=1),
                main_content,
            ],
            expand=True,
        )
    )

    # Exibir conteúdo inicial
    update_content(0)

ft.app(main)
