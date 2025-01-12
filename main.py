import flet as ft
import base64
import sqlite3





class DataBase():

    def fetch_images_from_db():
        # Conexão com o banco de dados
        conn = sqlite3.connect("seu_banco.db")
        cursor = conn.cursor()

        # Consulta para recuperar imagens
        cursor.execute("SELECT Image FROM sua_tabela LIMIT 30")
        rows = cursor.fetchall()
        conn.close()

        # Converte imagens binárias para formato base64
        images_base64 = [
            f"data:image/png;base64,{base64.b64encode(row[0]).decode()}" for row in rows
        ]
        return images_base64


# Classes para as funcionalidades
class Screen(ft.UserControl):
    def build(self):
        return ft.Text("Tela Base - Substitua em subclasses")

class EditScreen(Screen):

    def build(self):
        # Campos para inserir informações
        self.nome_produto = ft.TextField(label="Nome do Produto", width=800)
        self.Valor_Final = ft.TextField(label="De (R$) Por (R$)", keyboard_type="number", width=800)
        self.valor = ft.TextField(label="Valor (R$)", keyboard_type="number", width=800)
        self.Centavos = ft.TextField(label="Centavos", keyboard_type="number", width=800)
        self.Taxas = ft.TextField(label="Taxas", width=800)
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
            ], width=800
        )

        # Botão de salvar
        self.salvar_button = ft.ElevatedButton(
            text="Salvar",
            on_click=self.salvar_dados, width=150, height=50
        )

        # Layout dos campos
       # Layout dos campos
        # Layout dos campos
        return ft.Container(
            content=ft.Container(
                content=ft.Column(
                    [
                        self.nome_produto,
                        self.Valor_Final,
                        self.valor,
                        self.Centavos,
                         self.Taxas,
                        self.desconto,
                        self.codigo,
                        self.total_prazo,
                        self.tamanho_placa,
                        self.salvar_button,
                    ],
                    spacing=30,
                    alignment=ft.MainAxisAlignment.CENTER,  # Alinha os itens verticalmente no container interno
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Centraliza horizontalmente os itens
                ),
                alignment=ft.alignment.center,  # Centraliza o container interno
                border_radius=20,
                padding=20,  # Margem interna do container
                margin=ft.margin.all(10),
            ),
            padding=50,
            alignment=ft.alignment.center,  # Centraliza o container externo no centro da tela
            expand=True,  # Garante que o container externo ocupe todo o espaço disponível
            
        )
    

    def salvar_dados(self, e):
        # Captura os valores inseridos nos campos
        dados = {
            "nome_produto": self.nome_produto.value,
            "valor": self.valor.value,
            "desconto": self.desconto.value,
            "codigo": self.codigo.value,
            "total_prazo": self.total_prazo.value,
            "tamanho_placa": self.tamanho_placa.value,
        }

        # Exibe uma mensagem de sucesso (substitua por lógica para salvar os dados na imagem)
        print("Dados salvos:", dados)
        e.page.dialog = ft.AlertDialog(
            title=ft.Text("Sucesso"),
            content=ft.Text("Os dados foram salvos com sucesso!"),
            actions=[ft.TextButton("OK", on_click=lambda e: e.page.dialog.close())],
        )
        e.page.dialog.open = True
        e.page.update()
        
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
