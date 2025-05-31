import flet as ft
   
# Função principal
def main(page: ft.Page):
        
    page.padding = 0  # Remove qualquer padding adicional
    page.window_maximized = True
    
    # Função para alterar a tela exibida
    def update_content(index):
        screens = [
            Message(),
            Sendies(),
            Notifications(),
            SettingsScreen(page),
        ]
        main_content.content = screens[index]  # Usar .content em vez de .controls
        page.update()

    # Barra de navegação
    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        group_alignment=0.0,
        bgcolor="#222222",  # Cor de fundo escura
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.MESSAGE, selected_icon=ft.icons.MESSAGE,
                label="MENSAGENS",
                padding=ft.Padding(top=20, right=10, bottom=10, left=10),
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.SEND_ROUNDED, selected_icon=ft.icons.SEND_ROUNDED,
                label="ENVIADOS",
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
    main_content = ft.Container(expand=True)

    # Layout da barra de navegação à esquerda
    navigation_layout = ft.Container(
        rail, padding=10, height=500, width=200, border_radius=70, margin=25, bgcolor="#222222"
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
    
    def __init__(self):
        super().__init__()

    def build(self):
        return ft.Container(
            expand=True,
            content=ft.Text("Tela Base - Substitua em subclasses")
        )

class Message(Screen):

    def build(self):

        message_area = ft.Container(
            expand=True,
            bgcolor="#363232",
            border_radius=30,
            margin=5,
            padding=10,
            content=ft.Row(  # <- força o conteúdo interno a expandir horizontalmente
                expand=True,
                controls=[
                    ft.Text("Área de mensagens...", color="white", expand=True)
                ]
            )
        )

        Buttom = ft.Row(
            controls=[
                ft.TextField(
                hint_text="Digite sua mensagem...",
                bgcolor="#222222",
                border_radius=20,
                color="white",
                expand=True,  # Ocupa espaço restante
            ),
             ft.ElevatedButton("Enviar", bgcolor="#60923D", color="white", height=50, width=110),
             ft.ElevatedButton("Imagem", bgcolor="#1D7EBE", color="white", height=50, width=110),
            
            ],
             alignment=ft.MainAxisAlignment.CENTER,
             spacing=10,
        )

        # Container principal (esquerda)
        main_container = ft.Container(
            expand=True,
            bgcolor="#222222",
            # bgcolor="transparent",
            margin=10,
            padding=20,
            alignment=ft.alignment.center,
            border_radius=20,
            content=ft.Column(
                controls=[
                    ft.Text("Mensagens", size=20, weight=ft.FontWeight.BOLD, color="white"),
                    ft.Divider(height=10, color="#2C2C2C"),    
                    message_area,
                    Buttom
                ],
                spacing=10,
                expand=True,  # Garante que a coluna também se expanda   
            )
        )
        
        # Layout principal (duas colunas lado a lado)
         # Layout principal
        return ft.Row(
            expand=True,
            controls=[main_container],
        )
    
class Sendies(Screen):
   
    def build(self):
        return ft.Text("Tela de enviados", size=20)

class Notifications(Screen):
    def build(self):
        return ft.Text("Tela de alertas", size=20)
    
class SettingsScreen(ft.UserControl):
    
    def __init__(self, page, user=None):
        self.page = page
        super().__init__()
        
        self.date_picker = ft.DatePicker()
        page.overlay.append(self.date_picker)

        self.time_picker = ft.TimePicker()
        page.overlay.append(self.time_picker)

        self.user = user or {"name": "Usuário", "email": "email@example.com", "photo_url": ""}
        # Contêiner para o conteúdo dinâmico

        self.content_container = ft.Container(
            bgcolor="#222222",
            # expand=True, # removido para permitir que o container se expanda
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
   
    def change_theme_mode(self, e):
        """Alterna entre temas claro e escuro."""
        self.page.theme_mode = (
            ft.ThemeMode.LIGHT
            if self.page.theme_mode == ft.ThemeMode.DARK
            else ft.ThemeMode.DARK
        )
        self.page.update()
    
    def handle_change(e: ft.ControlEvent):
        print(f"change on panel with index {e.data}")

    def build(self):

        self.theme_switch = ft.Switch(label="  ESCURO/CLARO", thumb_icon=ft.icons.DARK_MODE, on_change=self.change_theme_mode)
        self.font_slider = ft.Slider(min=10, max=30, value=16, label="Tamanho da Fonte", on_change="change_font_size")
        
        self.theme_settings = ft.Container(
            bgcolor="#222222",
            # expand=True, # removido para permitir que o container se expanda
            border_radius=20,
            padding=20,
            margin=10,
            content=ft.Column(
                controls=[
                    ft.Text("Configurações de Tema", size=16, weight=ft.FontWeight.BOLD, color="white"),
                    ft.Divider(height=10, color="#2C2C2C"),
                    self.theme_switch,
                    ft.Divider(height=10, color="#2C2C2C"),
                    ft.Text("Configuração de Fonte", size=16,  weight=ft.FontWeight.BOLD, color="white"),
                    self.font_slider,
                ],
                expand=True,
                spacing=20,
            )
        )

        self.sendies_message = ft.Container(
            bgcolor="#222222",
            # expand=True, # removido para permitir que o container se expanda
            border_radius=20,
            padding=20,
            margin=10,
            content=ft.Column(
                controls=[
                    ft.Text("Programação de envio Data/Hora", size=16, weight=ft.FontWeight.BOLD, color="white"),
                    ft.Divider(height=10, color="#2C2C2C"),
                    ft.Row(
                        [
                            ft.ElevatedButton("DATA", width=110, height=50, on_click=lambda _: self.date_picker.pick_date()),
                            ft.ElevatedButton("HORA", width=110, height=50, on_click=lambda _: self.time_picker.pick_time()),
                        ]
                    ),
                    ft.Divider(height=10, color="#2C2C2C"),
                    ft.Text("Programação de envio por dia", size=16, weight=ft.FontWeight.BOLD, color="white"),
                    ft.Row(
                        [

                        ]
                    )
                    
                   
                ],
                expand=True,
                spacing=20,
            )
        )
    
        self.Information_additional = ft.Container(
            bgcolor="#222222",
            # height=500, # removido para permitir que o container se expanda
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

        self.Buttons_save_cancel = ft.Container(
            bgcolor="#222222",
            border_radius=20,
            padding=20,
            margin=10,
            content= ft.Column(
                    controls=[
                            ft.Row(
                                [
                                    ft.ElevatedButton("SALVAR", bgcolor="green", width=140, height=50),
                                    ft.ElevatedButton("CANCELAR", bgcolor="red", width=140, height=50)
                                ],
                        ),
                    ],                
                )
        )
 
        self.panel = ft.Container(
            content=ft.ExpansionPanelList(
                elevation=4,
                on_change=self.handle_change,
                controls=[
                    ft.ExpansionPanel(
                        bgcolor="#222222",
                        header=ft.Text("Termos e Avisos do Sistema", style="titleMedium", color="white"),
                        content=ft.Container(
                            content=ft.Text(
                                """
                               📄 Termo de Uso e Responsabilidade

                               
                                Este sistema foi desenvolvido com propósito exclusivamente profissional, visando otimizar processos e garantir maior produtividade ao contratante.
                                Ao utilizar este software, o usuário declara estar ciente e de acordo com os termos e condições descritos a seguir. Eventuais problemas decorrentes 
                                do uso indevido ou em desacordo com as diretrizes aqui estabelecidas não serão de responsabilidade dos desenvolvedores ou fornecedores do sistema.
                                Por favor, leia atentamente:

                                ⚠️ Regras de Uso e Responsabilidades
                                • Uso exclusivo: Este sistema é licenciado para uso exclusivo da pessoa ou empresa contratante. O repasse a terceiros, com ou sem fins lucrativos,
                                é expressamente proibido.

                                • Confidencialidade: Todos os dados inseridos e gerados são considerados confidenciais. O usuário se compromete a não divulgar, compartilhar ou vazar
                                qualquer informação gerada pelo sistema.

                                • Login pessoal: Não compartilhe seu login ou senha com terceiros. Cada usuário é responsável pelas ações realizadas com sua conta.

                                • Alterações indevidas: Usuários com conhecimento técnico avançado não devem alterar as configurações internas ou tentar modificar o funcionamento padrão
                                do sistema, sob risco de mau funcionamento ou perda de dados.

                                • Mensagens automáticas: O sistema utiliza o envio de mensagens pré-programadas para comunicação com clientes. O uso indevido, repetitivo ou com linguagem
                                inadequada pode resultar em bloqueio por parte da plataforma WhatsApp. Os desenvolvedores não se responsabilizam por sanções aplicadas por plataformas externas.

                                • Penalidades: O uso incorreto, abusivo ou que viole as leis vigentes poderá acarretar bloqueio imediato do acesso ao sistema, além de possíveis medidas judiciais.

                                • Segurança: É responsabilidade do usuário manter o ambiente seguro (evitar vírus, keyloggers, redes públicas inseguras) ao acessar o sistema.

                                • Backup de dados: Recomendamos que o usuário realize backups periódicos de suas informações, mesmo com funcionalidades automatizadas.

                                • Suporte técnico: O suporte será prestado apenas ao titular da licença ou aos contatos autorizados. Qualquer solicitação feita por terceiros poderá ser recusada.

                                • Atualizações: O sistema poderá receber atualizações automáticas. É responsabilidade do usuário manter a versão atualizada para garantir compatibilidade e segurança.

                                • Restrições legais: É expressamente proibido o uso do sistema para práticas ilegais, como spam, golpes, fraudes ou qualquer violação de normas éticas e legais.

                                ✅ Aceitação dos Termos
                                Ao utilizar este sistema, você declara ter lido, compreendido e aceito integralmente os termos acima descritos, isentando os desenvolvedores e fornecedores de qualquer
                                responsabilidade decorrente do uso indevido ou não autorizado da aplicação.

                                
                                                        """                                                       
                                                        ,
                                color="white",
                                size=14,
                            ),
                            padding=5,
                            alignment=ft.alignment.top_left,
                            # bgcolor="#333333",
                        ),
                        expanded=False
                    )
                ]
            ),
            bgcolor="#222222",
            border_radius=12,
            padding=20,
            margin=10
        )
    
        # Atualizando para ListView
        list_view = ft.ListView(
            controls=[
                self.build_google_account_container(),
                self.content_container,
                self.theme_settings,
                self.sendies_message,
                self.panel,
                self.Information_additional,
                self.Buttons_save_cancel,
               
            ],
            # expand=True, # Removido para permitir que o ListView se expanda
            padding=0,
            auto_scroll=True,  # Habilitar rolagem automática
        )
        
        return ft.Container(
            content=list_view,
            expand=True,
        )

ft.app(main, assets_dir="Image")