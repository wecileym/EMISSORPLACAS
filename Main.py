import flet as ft

   
# Função principal
def main(page: ft.Page):

    page.padding = 0  # Remove qualquer padding adicional
    page.window_maximized = True

    # Função para alterar a tela exibida
    def update_content(index):
        screens = [
            Dashboard(),
            ViewScreen(),
            DownloadScreen(),
            ChartScreen(),
            SettingsScreen(),
        ]
        main_content.controls.clear()  # Clear the content before appending new screen
        main_content.controls.append(screens[index])  # Append the new screen to the container
        page.update()

    # Barra de navegação
    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        group_alignment=0.0,
        bgcolor="#222222",  # Cor de fundo escura
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.INSERT_CHART, selected_icon=ft.icons.INSERT_CHART,
                label="DASHBOARD",
                padding=ft.Padding(top=20, right=10, bottom=10, left=10),
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.MONEY_OFF_OUTLINED, selected_icon=ft.icons.MONEY_OFF_OUTLINED,
                label="FINANCEIRO",
                padding=ft.Padding(top=20, right=10, bottom=10, left=10),
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.STORAGE, selected_icon=ft.icons.STORAGE,
                label="ESTOQUE",
                padding=ft.Padding(top=20, right=10, bottom=10, left=10),
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.NOTIFICATION_ADD, selected_icon=ft.icons.NOTIFICATION_ADD,
                label="ALERTAS",
                padding=ft.Padding(top=20, right=10, bottom=10, left=10),
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.SETTINGS, selected_icon=ft.icons.SETTINGS,
                label="CONFIGURAÇÃO",
                padding=ft.Padding(top=20, right=10, bottom=10, left=10),
            ),
        ],
        on_change=lambda e: update_content(e.control.selected_index),
    )

    # Contêiner principal para exibir as telas
    main_content = ft.Column(expand=True)

    # Layout da barra de navegação à esquerda
    navigation_layout = ft.Container(
        rail, padding=10, height=800, width=200, border_radius=50, margin=15, bgcolor="#222222"
    )

    # Layout principal com a barra de navegação e o conteúdo dinâmico
    main_layout = ft.Row(
        [
            navigation_layout,  # Barra de navegação à esquerda
            main_content,       # Layout de conteúdo à direita (expansível)
        ],
        expand=True,
    )

    # Função de login
    def show_main_app():
        page.controls.clear()
        page.add(main_layout)  # Adiciona a barra de navegação e o conteúdo principal
        update_content(0)      # Exibe a tela inicial (primeiro índice)

    # Exibe a tela de login inicialmente
    page.add(LoginScreen(on_login_success=show_main_app))
    
class LoginScreen(ft.UserControl):

    def __init__(self, on_login_success):
        super().__init__()
        self.on_login_success = on_login_success

    def build(self):
        
        # Container principal
        self.container = ft.Container(
            width=800,
            height=450,
            bgcolor="transparent",
            border_radius=20,
            padding=40,
            margin=220,
            content=self.login_content(),  # Define o conteúdo inicial da tela de login
        )
        
        st = ft.Stack(
            [
                ft.Image(
                    src=f"Image/pattern.png",
                    expand=True,
                    fit=ft.ImageFit.COVER,
                ),
                ft.Column(
                    controls=[
                        ft.Row(
                            controls=[self.container],
                            alignment=ft.MainAxisAlignment.CENTER,  # Centraliza o container na linha
                            expand=True  # Faz com que a Row ocupe toda a tela
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,  # Centraliza a coluna verticalmente
                    expand=True  # Expande para preencher a tela
                )
            ]
        )
        return st
    
    def show_create_account(self, e=None):
        """Alterna para o formulário de criação de conta."""
        self.container.content = self.create_account_content()
        self.update()

    def show_login(self, e=None):
        """Alterna para o formulário de login."""
        self.container.content = self.login_content()
        self.update()

    def create_account_content(self):
        return ft.Column(
            controls=[
                ft.Text("Criar nova conta.", size=28, weight=ft.FontWeight.BOLD, color="white"),
                ft.Text("Criar sua conta aqui!", color="gray"),
                ft.Row(
                    controls=[
                        ft.TextField(label="Nome", bgcolor="#363636", color="white", border_radius=15),
                        ft.TextField(label="Sobrenome", bgcolor="#363636", color="white", border_radius=15, width=410),
                    ]
                ),
                ft.TextField(label="Email", bgcolor="#363636", color="white", border_radius=15),
                ft.TextField(label="Senha", can_reveal_password=True, password=True, bgcolor="#363636", color="white", border_radius=15),
                ft.Divider(height=30, color="#2C2C2C"),
                ft.Row(
                    controls=[
                        ft.ElevatedButton("Cadastrar", bgcolor="green", color="white", height=50, width=150),
                        ft.ElevatedButton("Logar", bgcolor="blue", color="white", height=50, width=150, on_click=self.show_login),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                ),
            ]
        )

    def login_content(self):
        self.username = ft.TextField(label="Email", bgcolor="#363636", color="white", border_radius=15)
        self.password = ft.TextField(label="Senha", can_reveal_password=True, password=True, bgcolor="#363636", color="white", border_radius=15)
        self.error_message = ft.Text(value="", color="red")

        return ft.Column(
            controls=[
                ft.Text("Login", size=28, weight=ft.FontWeight.BOLD, color="white"),
                ft.Text("Você não tem uma conta?", color="gray"),
                self.username,
                self.password,
                self.error_message,
                ft.Divider(height=30, color="#2C2C2C"),
                ft.Row(
                    controls=[
                        ft.ElevatedButton("Entrar", bgcolor="blue", color="white", height=50, width=150, on_click=self.validate_login),
                        ft.ElevatedButton("Criar Conta", bgcolor="green", color="white", height=50, width=150, on_click=self.show_create_account),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                ),
            ]
        )

    def validate_login(self, e):
        """Simula a validação de usuário e senha."""
        username = self.username.value
        password = self.password.value

        # Validação de exemplo
        if username == "" and password == "":
            self.error_message.value = ""  # Limpar a mensagem de erro
            self.on_login_success()  # Chama o callback para sucesso no login
        else:
            self.error_message.value = "Usuário ou senha inválidos."
            self.update()  # Atualiza a tela para mostrar a mensagem de erro

# Classes para as funcionalidades
class Screen(ft.UserControl):
   
    def build(self):
        return ft.Text("Tela Base - Substitua em subclasses")

class Dashboard(Screen):

    def build(self):
        # Container principal (esquerda)
        main_container = ft.Container(
            expand=True,
            bgcolor="blue",
            margin=30,
            # height=950,
            alignment=ft.alignment.center,
            border_radius=30,
            content=ft.Column(
                controls=[
                    # Primeiro container (com dois dentro)
                    ft.Container(
                        bgcolor="red",
                        padding=20,
                        border_radius=15,
                        content=ft.Row(
                            controls=[
                                ft.Container(
                                    bgcolor="#444444",
                                    expand=True,
                                    height=150,
                                    border_radius=40,
                                ),
                                ft.Container(
                                    bgcolor="#555555",
                                    expand=True,
                                    height=150,
                                    border_radius=40,
                                ),
                            ],
                            # spacing=10
                        ),
                    ),

                    # Segundo container (com dois dentro)
                    ft.Container(
                        bgcolor="green",
                        padding=20,
                        border_radius=15,
                        content=ft.Row(
                            controls=[
                                ft.Container(
                                    bgcolor="#666666",
                                    expand=True,
                                    height=150,
                                    border_radius=40,
                                ),
                                ft.Container(
                                    bgcolor="#777777",
                                    expand=True,
                                    height=150,
                                    border_radius=40,
                                ),
                            ],
                            # spacing=10
                        )
                    ),

                    # Terceiro container
                    ft.Container(
                        bgcolor="#888888",
                        height=200,
                        border_radius=15,
                        alignment=ft.alignment.center,
                    ),
                ],
                # spacing=10
            )
        )
        
        ft.Divider(height=10, color="#2C2C2C"),
        
        # Coluna da direita (Perfil, Notificações, Gráficos)
        right_column = ft.Container(
            expand=True,
            bgcolor="#888888",
            border_radius=30,
            margin=20,
            # height=950,
            # width=230,
            content=ft.Column(  # Usamos Column para permitir múltiplos containers
                controls=[
                    # Perfil do usuário
                    ft.Container(
                        bgcolor="#222222",
                        height=150,
                        margin=5,
                        expand=True,
                        border_radius=30,
                        alignment=ft.alignment.center,
                        content=ft.Text("Profile", color="white")
                    ),

                    # Notificações
                    ft.Container(
                        bgcolor="#333333",
                        height=200,
                        margin=5,
                        expand=True,
                        border_radius=30,
                        alignment=ft.alignment.center,
                        content=ft.Text("Notifications", color="white")
                    ),

                    # Gráfico de sessões
                    ft.Container(
                        bgcolor="#444444",
                        expand=True,
                        height=200,
                        margin=5,
                        border_radius=30,
                        alignment=ft.alignment.center,
                        content=ft.Text("Device Sessions", color="white")
                    ),
                ],
                # spacing=10  # Espaçamento entre os containers
            ),
            # margin=20
        )

        # Layout principal (duas colunas lado a lado)
        return ft.Row(
            controls=[
                main_container,  # Esquerda
                right_column    # Direita
            ],
            # spacing=20
        )
    
class ViewScreen(Screen):
   
    def build(self):
        return ft.Text("Tela de Visualização", size=20)

class DownloadScreen(Screen):
    def build(self):
        return ft.Text("Tela de Downloads", size=20)

class ChartScreen(Screen):
    
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
                            color=ft.colors.AMBER,
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
                            color=ft.colors.BLUE,
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
                            color=ft.colors.RED,
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
                            color=ft.colors.ORANGE,
                            tooltip="Orange",
                            border_radius=0,
                        ),
                    ],
                ),
            ],
            border=ft.border.all(1, ft.colors.GREY_400),
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
                color=ft.colors.GREY_300, width=1, dash_pattern=[3, 3]
            ),
            tooltip_bgcolor=ft.colors.with_opacity(0.5, ft.colors.GREY_300),
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
    
class SettingsScreen(ft.UserControl):

    def __init__(self, user=None):

        super().__init__()
        

        self.user = user or {"name": "Usuário", "email": "email@example.com", "photo_url": ""}
        # Contêiner para o conteúdo dinâmico

        self.content_container = ft.Container(
            bgcolor="#222222",
            expand=True,
            margin=10,
            border_radius=20,
            padding=20,
            alignment=ft.alignment.center_left,  # Alinhando tudo para a esquerda
            content=ft.Column(
                controls=[
                    # Header
                    ft.Row(
                        controls=[
                            ft.Text("Perfil Detalhes", size=16, weight=ft.FontWeight.BOLD, color="white"),
                            ft.Container(
                                content=ft.Row(
                                    controls=[
                                        ft.Text("Este Ano", color="white"),
                                        ft.Icon(ft.icons.ARROW_DROP_DOWN, color="white"),
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                ),
                                bgcolor="#2C2C2C",
                                padding=10,
                                border_radius=10,
                            ),
                            ft.Container(
                                content=ft.Row(
                                    controls=[
                                        ft.Icon(ft.icons.DOWNLOAD, color="white"),
                                        ft.Text("Download Informações", color="white"),
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                ),
                                bgcolor="#00D1A0",
                                padding=10,
                                border_radius=10,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    ft.Divider(height=10, color="#2C2C2C"),
                    
                    # Profile Info
                    ft.Row(
                        controls=[
                            ft.CircleAvatar(
                                foreground_image_url="https://randomuser.me/api/portraits/women/45.jpg",
                                radius=40,
                            ),
                            ft.Column(
                                controls=[
                                    ft.Text("Natashia Khaleira", size=18, weight=ft.FontWeight.BOLD, color="white"),
                                    ft.Row(
                                        controls=[
                                            ft.Column(
                                                controls=[
                                                    ft.Text("Papel", color="gray"),
                                                    ft.Text("Vendedor(a)", color="white"),
                                                ]
                                            ),
                                            ft.Column(
                                                controls=[
                                                    ft.Text("Telefone", color="gray"),
                                                    ft.Text("(+62) 812 3456-7890", color="white"),
                                                ]
                                            ),
                                            ft.Column(
                                                controls=[
                                                    ft.Text("Endereço de Email", color="gray"),
                                                    ft.Text("natashiakhaleira@gmail.com", color="white"),
                                                ]
                                            ),
                                        ],
                                        spacing=30,
                                    )
                                ]
                            )
                        ],
                        spacing=20,
                    ),
                    
                    ft.Divider(height=10, color="#2C2C2C"),

                    # Stats
                    ft.Row(
                        controls=[
                            ft.Container(
                                content=ft.Column(
                                    controls=[
                                        ft.Icon(ft.icons.CHECK_CIRCLE, color="white"),
                                        ft.Text("309", size=16, weight=ft.FontWeight.BOLD, color="white"),
                                        ft.Text("Total Attendance", color="gray"),
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                ),
                                bgcolor="#363636",
                                border_radius=10,
                                padding=15,
                                width=150,
                            ),
                            ft.Container(
                                content=ft.Column(
                                    controls=[
                                        ft.Icon(ft.icons.ACCESS_TIME, color="white"),
                                        ft.Text("08:46", size=16, weight=ft.FontWeight.BOLD, color="white"),
                                        ft.Text("Avg Check In Time", color="gray"),
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                ),
                                bgcolor="#363636",
                                border_radius=10,
                                padding=15,
                                width=150,
                            ),
                            ft.Container(
                                content=ft.Column(
                                    controls=[
                                        ft.Icon(ft.icons.ACCESS_TIME, color="white"),
                                        ft.Text("17:04", size=16, weight=ft.FontWeight.BOLD, color="white"),
                                        ft.Text("Avg Check Out Time", color="gray"),
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                ),
                                bgcolor="#363636",
                                border_radius=10,
                                padding=15,
                                width=150,
                            ),
                            ft.Container(
                                content=ft.Column(
                                    controls=[
                                        ft.Icon(ft.icons.STAR, color="white"),
                                        ft.Text("Role Model", size=16, weight=ft.FontWeight.BOLD, color="white"),
                                        ft.Text("Employee Predicate", color="gray"),
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                ),
                                bgcolor="#363636",
                                border_radius=10,
                                padding=15,
                                width=150,
                            ),
                        ],
                        spacing=10,
                    )
                ],
                spacing=20,
            )
        )

    def build_google_account_container(self):

        return ft.Container(
            bgcolor="#222222",
            border_radius=20,
            padding=20,
            margin=10,
            content=ft.Column(
                controls=[
                    ft.Text("Conta do Google", size=16, weight=ft.FontWeight.BOLD, color="white"),
                    ft.Row(
                        controls=[
                            ft.CircleAvatar(
                                foreground_image_url=self.user.get("https://randomuser.me/api/portraits/women/45.jpg", ""),
                                radius=30,
                            ),
                            ft.Column(
                                controls=[
                                    ft.Text(self.user.get("name", "Usuário"),
                                            size=18, weight=ft.FontWeight.BOLD, color="white"),
                                    ft.Text(self.user.get("email", "email@example.com"), color="gray"),
                                ]
                            ),
                        ],
                        spacing=10,
                    ),
                    ft.Row(
                        controls=[
                            ft.ElevatedButton(
                                text="Trocar Conta",
                                on_click="self.switch_google_account",
                                bgcolor="#4F4F4F",
                                color="white",
                            ),
                            ft.ElevatedButton(
                                text="Alterar Nome",
                                on_click="self.change_display_name",
                                bgcolor="#4F4F4F",
                                color="white",
                            ),
                            ft.ElevatedButton(
                                text="Deslogar",
                                on_click='self.logout_google_account',
                                bgcolor="#4F4F4F",
                                color="white",
                            ),
                        ],
                        spacing=10,
                    )
                ],
                spacing=15,
            )
        )
    
    def build(self):

        self.theme_switch = ft.Switch(label="Tema Claro", on_change="self.change_theme")
        self.font_slider = ft.Slider(min=10, max=30, value=16, label="Tamanho da Fonte", on_change="change_font_size")
        
        self.theme_settings = ft.Container(
            bgcolor="#222222",
            expand=True,
            border_radius=20,
            padding=20,
            margin=10,
            content=ft.Column(
                controls=[
                    ft.Text("Configurações de Tema", size=16, weight=ft.FontWeight.BOLD, color="white"),
                    self.theme_switch,
                    self.font_slider,
                ],
                expand=True,
                spacing=20,
            )
        )
    
        self.additional_container = ft.Container(
            bgcolor="#222222",
            height=500,
            margin=10,
            padding=20,
            border_radius=30,
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Text("Backup Base de Dados", size=18, weight=ft.FontWeight.BOLD, color="white"),
                            ft.Icon(ft.icons.BACKUP, color="white"),
                        ]
                    ),
            ft.Divider(height=10, color="#2C2C2C"),

            # Row contendo duas colunas lado a lado
            ft.Row(
                controls=[
                    # Primeira coluna com dois containers menores
                    ft.Container(
                        bgcolor="#363636",
                        width=250,
                        height=390,
                        padding=5,
                        border_radius=30,
                        content=ft.Column(
                            controls=[
                                ft.Container(
                                    bgcolor="#363636",
                                    padding=10,
                                    border_radius=20,
                                    content=ft.ElevatedButton(
                                        text="DATA",
                                        on_click=lambda e: print("Data do Backup"),
                                        bgcolor="#4F4F4F",
                                        color="white",
                                        height=90,
                                        width=180,
                                        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=20),
                                        text_style=ft.TextStyle(size=20, weight=ft.FontWeight.BOLD),
                                        )
                                    ),
                                    alignment=ft.alignment.center
                                ),
                                ft.Container(
                                    bgcolor="#363636",
                                    padding=10,
                                    border_radius=20,
                                    content=ft.ElevatedButton(
                                        text="HORA",
                                        on_click=lambda e: print("Hora do Backup"),
                                        bgcolor="#4F4F4F",
                                        color="white",
                                        height=90,
                                        width=180,
                                        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=20),
                                        text_style=ft.TextStyle(size=20, weight=ft.FontWeight.BOLD),
                                        )
                                    ),
                                    alignment=ft.alignment.center                      
                                ),
                            ],
                            spacing=5,  # Reduzindo o espaço entre os botões
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                    ),

                    # Segunda coluna com um container que expande
                    ft.Container(
                        bgcolor="#2C2C2C",
                        expand=True,  # Faz o container ocupar todo o espaço restante
                        height=390,
                        margin=5,
                        padding=20,
                        border_radius=30,
                        content=ft.Text("Container maior que se expande", color="white"),
                    ),
                ]
            ),
        ],
        spacing=10,
    ),
)
        
        self.Information_additional = ft.Container(
            bgcolor="#222222",
            height=500,
            margin=10,
            padding=20,
            border_radius=30,
            content=ft.Column(
                controls=[
                    # Título no topo
                    ft.Row(
                        controls=[
                            ft.Text("INFORMAÇÕES ADICIONAIS", size=18, weight=ft.FontWeight.BOLD, color="white"),
                            ft.Icon(ft.icons.INFO, color="white"),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,  # Centraliza o título
                    ),

                    # Linha divisória
                    ft.Divider(height=10, color="#2C2C2C"),

                    # Logo centralizada
                    ft.Row(
                        controls=[
                            ft.Image(
                                src="Image/CODAR.png",  # Substitua pelo caminho correto da sua logo
                                width=120,
                                height=120,
                                fit=ft.ImageFit.CONTAIN,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,  # Centraliza a logo
                    ),

                    # Informações da empresa
                    ft.Row(
                        controls=[
                            ft.Text(
                                "CODAR SOLUÇÕES EM SOFTWARE\n\n"
                                "A CODAR é uma empresa especializada em desenvolvimento de software,\n "
                                "automação e análise de dados. Nosso objetivo é oferecer soluções tecnológicas "
                                "eficientes para empresas de todos\nos portes, ajudando a transformar desafios "
                                "em oportunidades.",
                                color="white",
                                size=14,
                                weight=ft.FontWeight.NORMAL,
                                text_align=ft.TextAlign.CENTER,  # Centraliza o texto
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),

                    # Redes sociais
                    ft.Row(
                        controls=[
                            ft.TextButton(
                                text="@codarsoftware",
                                on_click=lambda _: self.page.launch_url(
                                    "https://www.instagram.com/codarsoftware?igsh=d2Z4aGoyNTZ1aHpll"
                                ),
                                # style=ft.ButtonStyle(text_style=ft.TextStyle(color="#FF4081")),
                            ),
                            ft.TextButton(
                                text="codarsolucoessoftware@gmail.com",
                               
                            ),
                            ft.Icon(ft.icons.EMAIL_ROUNDED, color="white"),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,  # Centraliza o botão
                    ),
                ],
                spacing=10,  # Espaçamento entre os elementos
                alignment=ft.MainAxisAlignment.CENTER,  # Centraliza tudo dentro do Column
            ),
        )
    
        # Atualizando para ListView
        list_view = ft.ListView(
            controls=[
                self.build_google_account_container(),
                self.content_container,
                self.theme_settings,
                self.additional_container,
                self.Information_additional,
            ],
            expand=True,
            padding=20,
            auto_scroll=True,  # Habilitar rolagem automática se o conteúdo exceder a altura
            height=980,  # Adicionando altura fixa ao ListView
        )
        
        return list_view

ft.app(main, assets_dir="Image")