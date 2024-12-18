class Tarefa:
    def __init__(self, descricao, dificuldade, recompensa_ouro, recompensa_exp, status="Primária"):
        self.descricao = descricao
        self.dificuldade = dificuldade
        self.recompensa_ouro = recompensa_ouro
        self.recompensa_exp = recompensa_exp
        self.status = status

    def concluir(self, personagem):
        if self.status != "Concluída":
            self.status = "Concluída"
            mensagem_ouro = personagem.ganhar_ouro(self.recompensa_ouro)
            mensagem_exp = personagem.ganhar_experiencia(self.recompensa_exp)
            return f"Tarefa '{self.descricao}' concluída!\n{mensagem_ouro}\n{mensagem_exp}"
        else:
            return f"A tarefa '{self.descricao}' já foi concluída."

    def iniciar(self):
        if self.status == "Primária":
            self.status = "Em Progresso"
            return f"Tarefa '{self.descricao}' iniciada!"
        else:
            return f"A tarefa '{self.descricao}' já está em progresso ou concluída."

    def to_dict(self):
        return {
            "descricao": self.descricao,
            "dificuldade": self.dificuldade,
            "recompensa_ouro": self.recompensa_ouro,
            "recompensa_exp": self.recompensa_exp,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["descricao"],
            data["dificuldade"],
            data["recompensa_ouro"],
            data["recompensa_exp"],
            data.get("status", "Primária")
        )
