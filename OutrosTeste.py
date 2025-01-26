from screeninfo import get_monitors
import flet as ft

def main(page: ft.Page):
    # Tamanho da janela
    window_width = 900
    window_height = 700

    # Obter a resolução da tela usando screeninfo
    monitor = get_monitors()[0]  # Obtém o primeiro monitor
    screen_width = monitor.width
    screen_height = monitor.height

    # Calcula a posição para centralizar a janela
    window_left = (screen_width - window_width) // 2
    window_top = (screen_height - window_height) // 2

    # Configurações da janela
    page.title = "Edit Screen"
    page.window_width = window_width
    page.window_height = window_height
    page.window_left = window_left
    page.window_top = window_top
    page.window_resizable = False  # Evita redimensionar a janela
    page.add(EditScreen())

ft.app(target=main)
