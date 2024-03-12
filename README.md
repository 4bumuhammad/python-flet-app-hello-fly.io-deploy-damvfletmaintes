# Python : flet app hello fly.io deploy damvfletmaintest


files structure :

    ❯ tree -L 2 -I 'gambar-petunjuk|README.md'

        ├── Dockerfile
        ├── fly.toml
        ├── main.py
        └── requirements.txt


#### &#x1FAB6; code :

&#x1FAA7; Notes [enable clipboard on Vim] : 

- to select all lines in the vim editor is to press the `ggVG` key, then if you want to copy all the context, also press the `"+y` key. And if you want to paste it into the vim editor, you can do the key `"+p`.

- check 

    ❯ vim --version | grep clipboard

        +clipboard         -keymap            +printer           +vertsplit
        +eval              -mouse_jsbterm     -sun_workshop      -xterm_clipboard

- python

        ❯ vim main.py


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




- Dockerfile 

        ❯ vim Dockerfile


            FROM python:3-alpine

            WORKDIR /app

            COPY requirements.txt ./
            RUN pip install --no-cache-dir -r requirements.txt

            COPY . .

            EXPOSE 8080

            CMD ["python", "./main.py"]



#### &#x1F525; Test application with Docker container

    ❯ docker build -t flethello .

    ❯ docker run -d --name flethello-app -p 8080:8080 flethello


    # list

    ❯ docker images

        REPOSITORY   TAG       IMAGE ID       CREATED         SIZE
        flethello    latest    c2776a18e47f   6 seconds ago   143MB

    ❯ docker ps -a --format "table {{.ID}}\t{{.Image}}\t{{.Status}}\t{{.Names}}\t{{.Ports}}"

        CONTAINER ID   IMAGE       STATUS         NAMES           PORTS
        52eb0a6dc200   flethello   Up 4 seconds   flethello-app   0.0.0.0:8080->8080/tcp
---

#### Result :

<p align="center">
    <img src="./gambar-petunjuk/ss_flethello-app_container-1.png" alt="ss_flethello-app_container-1" style="display: block; margin: 0 auto;">
</p>


#### Reset containers :

    ❯ docker rm -f $(docker ps -aq) && docker rmi -f $(docker images -q)

---


<p align="center">
    <img src="./gambar-petunjuk/fly-io-logo.svg" alt="fly-io-logo" style="display: block; margin: 0 auto;">
</p>

---

## Stages in deploying the application to fly.io