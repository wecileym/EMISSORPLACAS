import flet as ft

class Dashboard(ft.UserControl):
    def build(self):
        # Sidebar fixa na lateral
        sidebar = ft.Container(
            width=200,
            bgcolor="#111111",
            border_radius=20,
            padding=10,
            content=ft.Column(
                tight=True,  # Ajusta exatamente ao tamanho dos itens internos
                controls=[
                    ft.Text("DASHBOARD", color="white"),
                    ft.Text("FINANCEIRO", color="white"),
                    ft.Text("ESTOQUE", color="white"),
                    ft.Text("ALERTAS", color="white"),
                    ft.Text("CONFIGURAÇÃO", color="white"),
                ],
            ),
        )

        # Área principal
        main_area = ft.Container(
            expand=True,
            content=ft.Column(
                tight=True,  # Não expande além dos elementos internos
                controls=[
                    ft.Container(bgcolor="red", height=60, border_radius=15),
                    ft.Container(bgcolor="blue", height=60, border_radius=15),
                    ft.Container(bgcolor="green", height=60, border_radius=15),
                ],
            ),
        )

        # Coluna da direita
        right_column = ft.Container(
            expand=True,
            content=ft.Column(
                tight=True,  # A coluna não cresce automaticamente, fica ajustada aos itens
                controls=[
                    ft.Container(bgcolor="#444444", height=50, border_radius=15, content=ft.Text("Profile", color="white")),
                    ft.Container(bgcolor="#555555", height=50, border_radius=15, content=ft.Text("Notifications", color="white")),
                    ft.Container(bgcolor="#666666", height=50, border_radius=15, content=ft.Text("Device Sessions", color="white")),
                ],
            ),
        )

        return ft.Row(
            expand=True,
            controls=[sidebar, main_area, right_column],
        )

def main(page: ft.Page):
    page.add(Dashboard())

ft.app(target=main)
