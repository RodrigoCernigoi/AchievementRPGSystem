import os
from flet import Page, Column, Row, Text, ElevatedButton, TextField, Tabs, Tab, AlertDialog
from modules.personagem import Personagem
from modules.tarefa import Tarefa
from modules.file_manager import salvar_dados, carregar_dados

ARQUIVO_DADOS = "data/dados_rpg.json"

class RPGInterface:
    def __init__(self, page: Page):
        self.page = page
        self.page.title = "Sistema de Tarefas RPG"

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

    def salvar_dados(self):
        dados = {
            "personagem": self.personagem.to_dict() if self.personagem else None,
            "tarefas": [t.to_dict() for t in self.lista_de_tarefas],
        }
        salvar_dados(ARQUIVO_DADOS, dados)

    def criar_interface_inicial(self):
        saudacao = self.obter_saudacao()

        container = Column(
            controls=[
                Text(saudacao, size=24, weight="bold"),
                ElevatedButton("Criar Personagem", on_click=self.criar_personagem),
                ElevatedButton(
                    "Ver Personagem",
                    on_click=self.ver_personagem,
                    disabled=not bool(self.personagem),
                ),
                ElevatedButton(
                    "Tarefas",
                    on_click=self.acessar_tarefas,
                    disabled=not bool(self.personagem),
                ),
                ElevatedButton("Criar Tarefa", on_click=self.criar_tarefa),
                ElevatedButton("Sair", on_click=lambda _: self.page.window_close()),
            ]
        )

        self.page.controls.clear()
        self.page.add(container)
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
            self.salvar_dados()
            dialog.open = False
            self.criar_interface_inicial()
            self.page.snack_bar = (Text("Personagem criado com sucesso!"))
            self.page.snack_bar.open = True
            self.page.update()

        input_nome = TextField(label="Nome do Personagem")
        input_classe = TextField(label="Classe do Personagem")
        dialog = AlertDialog(
            title=Text("Criar Personagem"),
            content=Column(
                controls=[input_nome, input_classe]
            ),
            actions=[ElevatedButton("Salvar", on_click=salvar_personagem)],
            open=True,
        )
        self.page.dialog = dialog
        self.page.update()

    def ver_personagem(self, e):
        container = Column(
            controls=[
                Text(f"Nome: {self.personagem.nome}"),
                Text(f"Classe: {self.personagem.classe}"),
                Text(f"Nível: {self.personagem.nivel}"),
                Text(f"Experiência: {self.personagem.experiencia}"),
                Text(f"Ouro: {self.personagem.ouro}"),
                Text("Itens:"),
                Column(
                    controls=[
                        Text(item) for item in self.personagem.itens
                    ] if self.personagem.itens else [Text("Nenhum item adquirido.")]
                ),
                ElevatedButton("Voltar", on_click=self.criar_interface_inicial),
            ]
        )

        self.page.controls.clear()
        self.page.add(container)
        self.page.update()

    def acessar_tarefas(self, e):
        tabs = Tabs(
            tabs=[
                Tab(text="Tarefas Primárias", content=self.listar_tarefas(self.tarefas_primarias)),
                Tab(text="Tarefas em Progresso", content=self.listar_tarefas(self.tarefas_em_progresso)),
                Tab(text="Tarefas Concluídas", content=self.listar_tarefas(self.tarefas_concluidas)),
            ]
        )
        voltar_button = ElevatedButton("Voltar", on_click=self.criar_interface_inicial)

        self.page.controls.clear()
        self.page.add(tabs, voltar_button)
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
                self.salvar_dados()
                self.acessar_tarefas(None)
                self.page.snack_bar = (Text("Tarefa concluída com sucesso!"))
                self.page.snack_bar.open = True
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
        self.page.overlay.append(dialog)
        self.page.update()

    def criar_tarefa(self, e):
        def salvar_tarefa(e):
            descricao = input_descricao.value
            dificuldade = input_dificuldade.value
            recompensa_ouro = int(input_ouro.value or 0)
            recompensa_exp = int(input_exp.value or 0)

            if not descricao or not dificuldade:
                dialog.content = Text("Todos os campos devem ser preenchidos!", color="red")
                self.page.update()
                return

            nova_tarefa = Tarefa(descricao, dificuldade, "Primária", recompensa_ouro, recompensa_exp)
            self.lista_de_tarefas.append(nova_tarefa)
            self.organizar_tarefas()
            self.salvar_dados()
            dialog.open = False
            self.criar_interface_inicial()
            self.page.snack_bar = (Text("Tarefa criada com sucesso!"))
            self.page.snack_bar.open = True
            self.page.update()

        input_descricao = TextField(label="Descrição da Tarefa")
        input_dificuldade = TextField(label="Dificuldade (1-5)")
        input_ouro = TextField(label="Recompensa em Ouro", keyboard_type="number")
        input_exp = TextField(label="Recompensa em Experiência", keyboard_type="number")
        dialog = AlertDialog(
            title=Text("Criar Tarefa"),
            content=Column(
                controls=[input_descricao, input_dificuldade, input_ouro, input_exp]
            ),
            actions=[ElevatedButton("Salvar", on_click=salvar_tarefa)],
            open=True,
        )
        self.page.overlay.append(dialog)
        self.page.update()

if __name__ == "__main__":
    from flet import app

    def main(page: Page):
        RPGInterface(page)

    app(target=main)
