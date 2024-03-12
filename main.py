import flet as ft

def main(page: ft.Page):


    appbar = ft.AppBar(
        title = ft.Text("Flet web app", size=45, color="white"),
        bgcolor = "blue"
    )

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    content_1 = ft.Container(
        content = ft.Column([
            ft.Text("Hello From Flet", size=40)
        ])
    )

    content_2 = ft.Container(
        content = ft.Column([
            ft.Text("by Dhony Abu Muhammad", size=20)
        ])
    )


    page.add(appbar, content_1, content_2)


ft.app(target=main, port=8080, view=None)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Berhasil
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
