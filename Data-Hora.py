import flet as ft

def main(page: ft.Page):
    page.title = "Agendamento de Mensagem"
    page.bgcolor = "#121212"
    page.theme_mode = ft.ThemeMode.DARK

    data_escolhida = ft.Text(value="Data: Nenhuma", color="white")
    hora_escolhida = ft.Text(value="Hora: Nenhuma", color="white")

    # # Calendário (DatePicker)
    # def on_date_selected(e):
    #     data_escolhida.value = f"Data: {e.control.value.strftime('%d/%m/%Y')}"
    #     page.update()

    date_picker = ft.DatePicker()
    page.overlay.append(date_picker)

    # # Relógio (TimePicker)
    # def on_time_selected(e):
    #     hora_escolhida.value = f"Hora: {e.control.value.strftime('%H:%M')}"
    #     page.update()

    time_picker = ft.TimePicker()
    page.overlay.append(time_picker)

    # Botões para abrir
    btn_data = ft.ElevatedButton(
        text="Escolher Data",
        on_click=lambda _: date_picker.pick_date(),
        bgcolor="#1C567D",
        color="white",
    )

    btn_hora = ft.ElevatedButton(
        text="Escolher Hora",
        on_click=lambda _: time_picker.pick_time(),
        bgcolor="#415533",
        color="white",
    )

    page.add(
        ft.Column(
            [
                data_escolhida,
                hora_escolhida,
                ft.Row([btn_data, btn_hora], spacing=20),
            ],
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
        )
    )

ft.app(target=main)
