import flet as ft

def main(page: ft.Page):
    # Variável com a imagem certa
    imagem_correta = "Buzz Lightyear"
    
    # Texto para feedback
    mensagem = ft.Text(
        f"Qual é o {imagem_correta}",
        text_align=ft.TextAlign.CENTER,
        size=20,
        height=50
    )

    # Função Jogar
    def jogar(e):
        imagem_selecionada = e.control.content.value
        if imagem_selecionada == imagem_correta:
            e.control.bgcolor = ft.Colors.PINK_200
            e.control.image.opacity = 0.3
            e.control.content.value = "😍"
            e.control.content.size = 40
            mensagem.value = "Parabéns! Você acertou."
        else:
            e.control.bgcolor = ft.Colors.BLUE_200
            e.control.image.opacity = 0.3
            e.control.content.value = "😢"
            e.control.content.size = 40
            mensagem.value = f"Ops! Não é o {imagem_correta}. Tente de novo."
        
        container_woody.on_click = None
        container_jessie.on_click = None
        container_buzzlightyear.on_click = None

        btn_jogar_novamente.visible = True

        page.update()
    
    # Função Jogar Novamente
    def jogar_novamente(e):
        btn_jogar_novamente.visible = False
        mensagem.value = f"Clique no {imagem_correta}"

        container_woody.image.opacity = 1.0
        container_woody.on_click = jogar
        container_woody.content.size = 0
        container_woody.content.value = "Woody"

        container_jessie.image.opacity = 1.0
        container_jessie.on_click = jogar
        container_jessie.content.size = 0
        container_jessie.content.value = "Jessie"

        container_buzzlightyear.image.opacity = 1.0
        container_buzzlightyear.on_click = jogar
        container_buzzlightyear.content.size = 0
        container_buzzlightyear.content.value = "Buzz Lightyear"
        
        page.update()

    # Container Woody
    container_woody = ft.Container(
        content=ft.Text(
            "Woody",
            size=0
        ),
        image=ft.DecorationImage(
            src="images/woody.jpg",
            fit=ft.BoxFit.COVER
        ),
        width=100,
        height=100,
        margin=10,
        bgcolor=ft.Colors.GREY_200,
        border_radius=10,
        alignment=ft.Alignment(0, 0),
        ink=True,
        on_click=jogar
    )
    # Container Jessie
    container_jessie = ft.Container(
        content=ft.Text(
            "Jessie",
            size=0
        ),
        image=ft.DecorationImage(
            src="images/jessie.jpg",
            fit=ft.BoxFit.COVER
        ),
        width=100,
        height=100,
        margin=10,
        bgcolor=ft.Colors.GREY_200,
        border_radius=10,
        alignment=ft.Alignment(0, 0),
        ink=True,
        on_click=jogar
    )

    # Container Buzz Lightyear
    container_buzzlightyear = ft.Container(
        content=ft.Text(
            "Buzz Lightyear",
            size=0
        ),
        image=ft.DecorationImage(
            src="images/buzz.webp",
            fit=ft.BoxFit.COVER
        ),
        width=100,
        height=100,
        margin=10,
        bgcolor=ft.Colors.GREY_200,
        border_radius=10,
        alignment=ft.Alignment(0, 0),
        ink=True,
        on_click=jogar
    )

    # Botão "Jogar Novamente"
    btn_jogar_novamente = ft.Button(
        "Jogar Novamente",
        visible=False,
        on_click=jogar_novamente
    )
    page.title = "Flet Toy Story"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = "#97e4f7"
    page.add(
        ft.Column(
            [
                ft.Text(
                    "Selecione a imagem certa",
                    size=24,
                    weight="bold",
                    color="#051775"
                ),
                mensagem,
                ft.Row(
                    [
                        container_woody,
                        container_jessie,
                        container_buzzlightyear
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                btn_jogar_novamente
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
    )

ft.run(main)