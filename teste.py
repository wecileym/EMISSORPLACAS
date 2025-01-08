import flet as ft


def main(page: ft.Page):

    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        # extended=True,
        min_width=100,
        min_extended_width=400,
        group_alignment=0.0,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.Icon(ft.Icons.CREATE_NEW_FOLDER, size=40),
                label="EDITAR",
            ),
            
            ft.NavigationRailDestination(
                icon=ft.Icon(ft.Icons.VISIBILITY, size=40),
                label_content=ft.Text("VISUALIZAÇÃO"),
            ),
            ft.NavigationRailDestination(
                icon=ft.Icon(ft.Icons.DOWNLOAD, size=40),
                label_content=ft.Text("DOWNLOADS"),
            ),
            ft.NavigationRailDestination(
                icon=ft.Icon(ft.Icons.SHOW_CHART, size=40),
                label_content=ft.Text("GRÁFICOS"),
            ),
            ft.NavigationRailDestination(
                icon=ft.Icon(ft.Icons.SETTINGS, size=40),
                label_content=ft.Text("CONFIGURAÇÃO"),
                
            )
        ],
        on_change=lambda e: print("Selected destination:", e.control.selected_index),
    )

    page.add(
        ft.Row(
            [
                rail,
                ft.VerticalDivider(width=1),
            ],
            expand=True,
                    
        )
    )

ft.app(main)