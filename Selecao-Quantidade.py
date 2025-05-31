import flet as ft


def main(page: ft.Page):
    colors = [
        ft.colors.RED,
        ft.colors.BLUE,
        ft.colors.YELLOW,
        ft.colors.PURPLE,
        ft.colors.LIME,
    ]

    def get_options():
        options = []
        for color in colors:
            options.append(
                ft.DropdownOption(
                    key=color.value,
                    content=ft.Text(
                        value=color.value,
                        color=color,
                    ),
                )
            )
        return options

    def dropdown_changed(e):
        e.control.color = e.control.value
        page.update()

    dd = ft.Dropdown(
        editable=True,
        label="Color",
        options=get_options(),
        on_change=dropdown_changed,
    )

    page.add(dd)


ft.app(main)