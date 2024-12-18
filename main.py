import os
import locale
from flet import Page, Column, Row, Text, ElevatedButton, TextField, Dropdown, dropdown, AlertDialog, Tab, Tabs, Container, alignment, Animation, transform, Colors
from modules.personagem import Personagem
from modules.tarefa import Tarefa
from modules.gacha import Gacha
from modules.file_manager import salvar_dados, carregar_dados

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
os.environ["LANG"] = "pt_BR.UTF-8"
os.environ["LC_ALL"] = "pt_BR.UTF-8"


ARQUIVO_DADOS = "data/dados_rpg.json"

class RPGInterface:
    def __init__(self, page: Page):
        self.page = page
        self.page.title = "Sistema de Tarefas RPG"
        self.page.theme_mode = "light"
        self.page.horizontal_alignment = "center"
        self.page.vertical_alignment = "center"

        # Carregar dados
        self.dados = carregar_dados(ARQUIVO_DADOS)
        if self.dados:
            self.personagem = Personagem.from_dict(self.dados["personagem"])
            self.lista_de_tarefas = [Tarefa.from_dict(t) for t in self.dados["tarefas"]]
        else:
            self.personagem = None
            self.lista_de_tarefas = []

        self.tarefas_primarias = []
        self.tarefas_em_progresso = []
        self.tarefas_concluidas = []

        self.organizar_tarefas()
        self.criar_interface_inicial()

    def organizar_tarefas(self):
        self.tarefas_primarias = [t for t in self.lista_de_tarefas if t.status == "Primária"]
        self.tarefas_em_progresso = [t for t in self.lista_de_tarefas if t.status == "Em Progresso"]
        self.tarefas_concluidas = [t for t in self.lista_de_tarefas if t.status == "Concluída"]

    def criar_interface_inicial(self):
        self.page.views.clear()
        saudacao = self.obter_saudacao()

        # Animação de fade in
        container = Container(
            content=Column(
                controls=[
                    Text(saudacao, size=24, weight="bold", color=Colors.BLUE),
                    ElevatedButton("Criar Personagem", on_click=self.criar_personagem),
                    ElevatedButton(
                        "Acessar Menu",
                        on_click=self.acessar_menu,
                        disabled=not bool(self.personagem),
                    ),
                    ElevatedButton("Sair", on_click=lambda _: self.page.window_close()),
                ],
                alignment="center",
                horizontal_alignment="center",
            ),
            alignment=alignment.center,
            animate_opacity=300,
            opacity=0,  # Inicialmente invisível
        )

        self.page.add(container)
        container.opacity = 1  # Ajusta a opacidade para fazer o fade in
        self.page.update()

    def obter_saudacao(self):
        from datetime import datetime
        hora = datetime.now().hour
        if hora < 12:
            return "Bom dia! Bem-vindo ao Sistema de Tarefas RPG!"
        elif hora < 18:
            return "Boa tarde! Bem-vindo ao Sistema de Tarefas RPG!"
        else:
            return "Boa noite! Bem-vindo ao Sistema de Tarefas RPG!"

    def criar_personagem(self, e):
        def salvar_personagem(e):
            nome = input_nome.value
            classe = input_classe.value

            if not nome or not classe:
                dialog.content = Text("Todos os campos devem ser preenchidos!", color="red")
                self.page.update()
                return

            self.personagem = Personagem(nome, classe)
            self.lista_de_tarefas = []
            self.organizar_tarefas()
            dialog.open = False
            self.page.snack_bar = AlertDialog(title=Text(f"Personagem {nome} criado com sucesso!"))
            self.page.snack_bar.open = True
            self.criar_interface_inicial()
            self.page.update()

        input_nome = TextField(label="Nome do Personagem")
        input_classe = TextField(label="Classe do Personagem")
        dialog = AlertDialog(
            title=Text("Criar Personagem"),
            content=Column(
                controls=[input_nome, input_classe], spacing=10
            ),
            actions=[ElevatedButton("Salvar", on_click=salvar_personagem)],
            open=True,
        )
        self.page.dialog = dialog
        self.page.update()

    def acessar_menu(self, e):
        self.page.views.clear()
        tabs = Tabs(
            tabs=[
                Tab(text="Tarefas Primárias", content=self.listar_tarefas(self.tarefas_primarias)),
                Tab(text="Tarefas em Progresso", content=self.listar_tarefas(self.tarefas_em_progresso)),
                Tab(text="Tarefas Concluídas", content=self.listar_tarefas(self.tarefas_concluidas)),
            ]
        )
        # Animação de deslizar tabs
        container = Container(
            content=tabs,
            alignment=alignment.center,
            animate_position=300,
            animate_opacity=300,
            position=transform.Offset(-1, 0),  # Inicializa fora da tela
        )
        voltar_button = ElevatedButton("Voltar", on_click=lambda _: self.criar_interface_inicial())
        self.page.add(container, voltar_button)

        # Anima o container para deslizá-lo para o centro
        container.position = transform.Offset(0, 0)
        self.page.update()

    def listar_tarefas(self, tarefas):
        return Column(
            controls=[
                ElevatedButton(
                    f"{i+1}. {t.descricao} - {t.status}",
                    on_click=lambda _, t=t: self.detalhar_tarefa(t),
                )
                for i, t in enumerate(tarefas)
            ]
        )

    def detalhar_tarefa(self, tarefa):
        def concluir_tarefa(e):
            if tarefa.status != "Concluída":
                tarefa.status = "Concluída"
                self.organizar_tarefas()
                self.page.snack_bar = AlertDialog(title=Text(f"Tarefa '{tarefa.descricao}' concluída!"))
                self.page.snack_bar.open = True
                self.acessar_menu(None)
                self.page.update()

        dialog = AlertDialog(
            title=Text("Detalhes da Tarefa"),
            content=Column(
                controls=[
                    Text(f"Descrição: {tarefa.descricao}"),
                    Text(f"Dificuldade: {tarefa.dificuldade}"),
                    Text(f"Recompensa: {tarefa.recompensa_ouro} ouro, {tarefa.recompensa_exp} exp"),
                    Text(f"Status: {tarefa.status}"),
                ]
            ),
            actions=[ElevatedButton("Concluir", on_click=concluir_tarefa)],
            open=True,
        )
        self.page.dialog = dialog
        self.page.update()

if __name__ == "__main__":
    from flet import app

    def main(page: Page):
        page.locale = "pt_BR"
        RPGInterface(page)

    app(target=main)
