import flet as ft
import base64
import sqlite3  # ou a biblioteca de banco de dados que você está usando

# Função para buscar imagens do banco de dados
def fetch_images_from_db():
    # Conexão com o banco de dados
    conn = sqlite3.connect("seu_banco.db")
    cursor = conn.cursor()

    # Consulta para recuperar imagens
    cursor.execute("SELECT imagem FROM sua_tabela LIMIT 30")
    rows = cursor.fetchall()
    conn.close()

    # Converte imagens binárias para formato base64
    images_base64 = [
        f"data:image/png;base64,{base64.b64encode(row[0]).decode()}" for row in rows
    ]
    return images_base64

def main(page: ft.Page):
    page.title = "Visualização de Placas"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20
    page.scroll = "always"  # Permitir rolagem na página caso necessário
    page.update()

    # Contêiner para as imagens em um layout espaçoso
    image_gallery = ft.GridView(
        expand=1,  # Expande para ocupar o espaço disponível
        max_extent=400,  # Define o tamanho máximo de cada "célula" (imagens grandes)
        child_aspect_ratio=1,  # Mantém as imagens quadradas
        spacing=20,  # Espaço entre as imagens
        run_spacing=20,  # Espaço entre as linhas
    )

    # Busca imagens do banco de dados
    images_from_db = fetch_images_from_db()

    # Adiciona as imagens recuperadas ao GridView
    for img_src in images_from_db:
        image_gallery.controls.append(
            ft.Image(
                src=img_src,
                width=400,  # Largura grande para a visualização
                height=400,  # Altura correspondente
                fit=ft.ImageFit.COVER,  # Ajusta a imagem para preencher sem distorcer
                border_radius=ft.border_radius.all(15),  # Bordas arredondadas
            )
        )

    # Adiciona a galeria de imagens à página
    page.add(image_gallery)
    page.update()

ft.app(main)
