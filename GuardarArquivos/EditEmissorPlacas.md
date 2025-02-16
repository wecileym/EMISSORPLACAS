# Definição dos campos
        self.nome_produto = ft.TextField(label="Nome do Produto")
        self.valor_final = ft.TextField(label="De (R$) Por (R$)", icon=ft.icons.MONEY)
        self.valor = ft.TextField(label="Valor (R$)", icon=ft.icons.MONEY)
        self.centavos = ft.TextField(label="Centavos", icon=ft.icons.FORMAT_LIST_NUMBERED)
        self.taxas = ft.TextField(label="Taxas", icon=ft.icons.SELL)
        self.desconto = ft.TextField(label="Desconto (%)", icon=ft.icons.PERCENT)
        self.codigo = ft.TextField(label="Código do Produto", icon=ft.icons.QR_CODE)
        self.total_prazo = ft.TextField(label="Total a Prazo (R$)", icon=ft.icons.TIMER)
        self.tamanho_placa = ft.Dropdown(
            label="Tamanho da Placa",
            options=[
                ft.dropdown.Option("Mini"),
                ft.dropdown.Option("Pequeno"),
                ft.dropdown.Option("Médio"),
                ft.dropdown.Option("Grande"),
                
            ],
            icon=ft.icons.VIEW_COLUMN,  # Ícone substituído por um válido
        )

        # Layout principal
        return ft.Column(

            controls=[
                # Título da Tela (Centralizado)
                ft.Container(
                    content=ft.Text(
                        "EMISSOR DE PLACAS",
                        size=40,
                        weight=ft.FontWeight.BOLD,
                        color=ft.colors.WHITE12,
                    ),
                    padding=40,
                    alignment=ft.alignment.center,  # Centraliza o título
                ),
                # Formulário de entrada
                ft.Card(
                    content=ft.Container(
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
                        ),
                        margin=30,
                        padding=10,
                        bgcolor="transparent",
                        border_radius=20,
                    ),
                ),
                # Botões
                ft.Row(
                    [
                        ft.ElevatedButton(
                            "Salvar",
                            icon=ft.icons.CHECK,
                            bgcolor=ft.colors.GREEN,
                            color=ft.colors.WHITE,
                            on_click=self.salvar_dados,
                            width=150,
                            height=50,
                        ),
                        ft.ElevatedButton(
                            "Cancelar",
                            icon=ft.icons.CLOSE,
                            bgcolor=ft.colors.RED,
                            color=ft.colors.WHITE,
                            on_click=self.Cancelado,
                            width=150,
                            height=50,                            
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.START,  # Alinha os botões à direita
                    spacing=10,
                ),
            ],
            spacing=10,  # Espaçamento geral entre os elementos na coluna
        )

    def salvar_dados(self, e):
        dados = {
            "nome_produto": self.nome_produto.value,
            "valor_final": self.valor_final.value,
            "valor": self.valor.value,
            "centavos": self.centavos.value,
            "taxas": self.taxas.value,
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
        print("Operação cancelada.")
        e.page.snack_bar = ft.SnackBar(ft.Text("Operação cancelada!"))
        e.page.snack_bar.open = True
        e.page.update()
