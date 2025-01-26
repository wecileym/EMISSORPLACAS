import flet as ft

import flet as ft

class ChartScreen(ft.UserControl):
    def build(self):
        # Função chamada quando a página for redimensionada
        def on_resize(e):
            # Obtém a altura da tela
            screen_height = self.page.height

            # Atualiza a altura do gráfico com base na altura da tela
            chart.height = screen_height * 0.6  # O gráfico ocupará 60% da altura da tela
            self.update()  # Atualiza o componente

        # Criando o gráfico de barras
        chart = ft.BarChart(
            bar_groups=[
                ft.BarChartGroup(
                    x=0,
                    bar_rods=[
                        ft.BarChartRod(
                            from_y=0,
                            to_y=40,
                            width=40,
                            color=ft.Colors.AMBER,
                            tooltip="Apple",
                            border_radius=0,
                        ),
                    ],
                ),
                ft.BarChartGroup(
                    x=1,
                    bar_rods=[
                        ft.BarChartRod(
                            from_y=0,
                            to_y=100,
                            width=40,
                            color=ft.Colors.BLUE,
                            tooltip="Blueberry",
                            border_radius=0,
                        ),
                    ],
                ),
                ft.BarChartGroup(
                    x=2,
                    bar_rods=[
                        ft.BarChartRod(
                            from_y=0,
                            to_y=30,
                            width=40,
                            color=ft.Colors.RED,
                            tooltip="Cherry",
                            border_radius=0,
                        ),
                    ],
                ),
                ft.BarChartGroup(
                    x=3,
                    bar_rods=[
                        ft.BarChartRod(
                            from_y=0,
                            to_y=60,
                            width=40,
                            color=ft.Colors.ORANGE,
                            tooltip="Orange",
                            border_radius=0,
                        ),
                    ],
                ),
            ],
            border=ft.border.all(1, ft.Colors.GREY_400),
            left_axis=ft.ChartAxis(
                labels_size=40, title=ft.Text("Fruit supply"), title_size=40
            ),
            bottom_axis=ft.ChartAxis(
                labels=[
                    ft.ChartAxisLabel(
                        value=0, label=ft.Container(ft.Text("Apple"), padding=10)
                    ),
                    ft.ChartAxisLabel(
                        value=1, label=ft.Container(ft.Text("Blueberry"), padding=10)
                    ),
                    ft.ChartAxisLabel(
                        value=2, label=ft.Container(ft.Text("Cherry"), padding=10)
                    ),
                    ft.ChartAxisLabel(
                        value=3, label=ft.Container(ft.Text("Orange"), padding=10)
                    ),
                ],
                labels_size=40,
            ),
            horizontal_grid_lines=ft.ChartGridLines(
                color=ft.Colors.GREY_300, width=1, dash_pattern=[3, 3]
            ),
            tooltip_bgcolor=ft.Colors.with_opacity(0.5, ft.Colors.GREY_300),
            max_y=110,
            interactive=True,
            expand=True,  # Faz o gráfico ocupar todo o espaço disponível
        )

        # Registra o evento de redimensionamento da página
        self.page.on_resize = on_resize

        # Retorna o Container com o gráfico
        return ft.Container(
            content=chart,
            padding=50,
            expand=True,
            alignment=ft.alignment.center,
            height=self.page.height * 0.6,  # Inicializa com 60% da altura da tela
        )


def main(page: ft.Page):
    # Inicializa o sistema com ChartScreen
    page.title = "Gráfico de Barras"
    page.add(ChartScreen())  # Adiciona a tela principal


ft.app(main)


# Configuração para iniciar a aplicação
ft.app(target=build)
