import flet as ft
from FunctionsDataBase import DataBase
   


# Função principal
def main(page: ft.Page):

    page.padding = 0  # Remove qualquer padding adicional

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
               padding=ft.Padding(top=20, right=10, bottom=10, left=10),
            ),
            ft.NavigationRailDestination(
                icon=ft.Icon(ft.Icons.VISIBILITY, size=40),
                label="VISUALIZAÇÃO",
               padding=ft.Padding(top=20, right=10, bottom=10, left=10),
            ),
            ft.NavigationRailDestination(
                icon=ft.Icon(ft.Icons.DOWNLOAD, size=40),
                label="DOWNLOADS",
               padding=ft.Padding(top=20, right=10, bottom=10, left=10),
            ),
            ft.NavigationRailDestination(
                icon=ft.Icon(ft.Icons.SHOW_CHART, size=40),
                label="GRÁFICOS",
               padding=ft.Padding(top=20, right=10, bottom=10, left=10),
            ),
            ft.NavigationRailDestination(
                icon=ft.Icon(ft.Icons.SETTINGS, size=40),
                label="CONFIGURAÇÃO",
               padding=ft.Padding(top=20, right=10, bottom=10, left=10),
            ),
        ],
        on_change=lambda e: update_content(e.control.selected_index),
        
    )

    # Contêiner principal para exibir as telas
    main_content = ft.Column(expand=True)

    # Layout principal com a barra de navegação e o conteúdo dinâmico
    
    main_layout = ft.Row(
        [
            rail,
            ft.VerticalDivider(width=1),
            main_content,
        ],
        expand=True,
    )

    # Função de login
    def show_main_app():
        page.controls.clear()
        page.add(main_layout)  # Adiciona o layout principal após o login
        update_content(0)      # Exibe a tela inicial (primeiro índice)

    # Exibe a tela de login inicialmente
    page.add(LoginScreen(on_login_success=show_main_app))
    
class LoginScreen(ft.UserControl):
     
     def __init__(self, on_login_success):

        super().__init__()
        self.on_login_success = on_login_success

     def build(self):

        self.username = ft.TextField(label="Usuário", width=400)
        self.password = ft.TextField(
            label="Senha", password=True, can_reveal_password=True, width=400,
        )
        self.login_button = ft.ElevatedButton(
            text="Entrar", on_click=self.validate_login, width=400, height=50, bgcolor="green"
        )
        self.login_with_google = ft.ElevatedButton(
            text="Google",
            bgcolor="white",
            width=400,
            height=50,
            icon=ft.Image(
                src="Image/Google.webp",  # URL ou caminho local da imagem
                width=400,
                height=80,
                fit=ft.ImageFit.CONTAIN,
            )
            
        )

        self.error_message = ft.Text(value="", color="red")

         # Layout principal com imagem de fundo
        
        return ft.Stack(
            [
                # Imagem de fundo
                ft.Image(
                    src="Image/pattern.png",  # Caminho da imagem de fundo
                    fit=ft.ImageFit.COVER,
                    expand=True,  # Preenche toda a tela
                ),
                # Conteúdo da tela de login
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text("Tela de Login", size=24, weight="bold", color="white"),
                            self.username,
                            self.password,
                            self.login_button,
                            self.login_with_google,
                            self.error_message,
                        ],
                        spacing=10,
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    alignment=ft.alignment.center,
                    padding=280
                ),
            ],
            expand=True,  # Garante que o Stack preencha a tela
        )
        
     
     def validate_login(self, e):
        # Simula uma validação de usuário e senha
        username = self.username.value
        password = self.password.value

        if username == "admin" and password == "1234":
            self.on_login_success()
        else:
            self.error_message.value = "Usuário ou senha inválidos."
            self.update()

# Classes para as funcionalidades
class Screen(ft.UserControl):
    def build(self):
        return ft.Text("Tela Base - Substitua em subclasses")

class EditScreen(ft.UserControl):  # Alterado para UserControl

    def build(self):
        # Campos para inserir informações
        self.nome_produto = ft.TextField(label="Nome do Produto", width=800)
        self.valor_final = ft.TextField(label="De (R$) Por (R$)", keyboard_type="number", width=800)
        self.valor = ft.TextField(label="Valor (R$)", keyboard_type="number", width=800)
        self.centavos = ft.TextField(label="Centavos", keyboard_type="number", width=800)
        self.taxas = ft.TextField(label="Taxas", width=800)
        self.desconto = ft.TextField(label="Desconto (%)", keyboard_type="number", width=800)
        self.codigo = ft.TextField(label="Código do Produto", width=800)
        self.total_prazo = ft.TextField(label="Total a Prazo (R$)", keyboard_type="number", width=800)

        # Campo para selecionar o tamanho da placa
        self.tamanho_placa = ft.Dropdown(
            label="Tamanho da Placa",
            options=[
                ft.dropdown.Option("Mini"),
                ft.dropdown.Option("Pequena"),
                ft.dropdown.Option("Média"),
                ft.dropdown.Option("Grande"),
            ],
            width=800,
        )

        # Botões
        self.salvar_button = ft.ElevatedButton(
            text="Salvar",
            on_click=self.salvar_dados,
            height=50,
            width=392,
            bgcolor="green",
        )
        self.cancelar_button = ft.ElevatedButton(
            text="Cancelar",
            on_click=self.Cancelado,
            height=50,
            width=392,
            bgcolor="red",
            
        )

        # Layout principal ajustado para a parte inferior
        return ft.Container(
            content=ft.Column(
                [
                    # Campos organizados
                    ft.Column(
                        [
                            self.nome_produto,
                            self.valor_final,
                            self.valor,
                            self.centavos,
                            self.taxas,
                            self.desconto,
                            self.codigo,
                            self.total_prazo,
                            self.tamanho_placa,
                        ],
                        spacing=15,
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    # Botões alinhados na parte inferior
                    ft.Row(
                        [
                            self.salvar_button,
                            self.cancelar_button,
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                ],
                spacing=50,  # Espaçamento entre os campos e botões
                alignment=ft.MainAxisAlignment.END,  # Move tudo para baixo
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            padding=130,
            alignment=ft.alignment.center,  # Centraliza horizontalmente
            expand=True,  # Expande o container para ocupar a tela inteira
        )

    def salvar_dados(self, e):
        dados = {
            "nome_produto": self.nome_produto.value,
            "valor": self.valor.value,
            "desconto": self.desconto.value,
            "codigo": self.codigo.value,
            "total_prazo": self.total_prazo.value,
            "tamanho_placa": self.tamanho_placa.value,
        }
        print("Dados salvos:", dados)
        e.page.snack_bar = ft.SnackBar(ft.Text("Dados salvos com sucesso!"))
        e.page.snack_bar.open = True
        e.page.update()

    def Cancelado(self, e):
        dados = {
            "nome_produto": self.nome_produto.value,
            "valor": self.valor.value,
            "desconto": self.desconto.value,
            "codigo": self.codigo.value,
            "total_prazo": self.total_prazo.value,
            "tamanho_placa": self.tamanho_placa.value,
        }
        print("Dados Cancelados:", dados)
        e.page.snack_bar = ft.SnackBar(ft.Text("Dados Cancelados!"))
        e.page.snack_bar.open = True
        e.page.update()
        
class ViewScreen(Screen):
    def build(self):
        return ft.Text("Tela de Visualização", size=20)

class DownloadScreen(Screen):
    def build(self):
        return ft.Text("Tela de Downloads", size=20)

class ChartScreen(ft.UserControl):

   def build(self):
        
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
        
        # Coloca o gráfico dentro de um Container para expandir e ocupar a tela inteira

        return ft.Container(
                content=chart,
                padding=50,  # Defina o padding para ajustar a distância
                expand=True,  # Garante que o gráfico vai expandir e ocupar toda a tela
                alignment=ft.alignment.center, # Centraliza o gráfico
                height=1000,
            )
        
class SettingsScreen(Screen):
    def build(self):
        return ft.Text("Tela de Configuração", size=20)


ft.app(main, assets_dir="Image")
