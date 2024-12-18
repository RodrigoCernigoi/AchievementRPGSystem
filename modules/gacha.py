import random

class Gacha:
    def __init__(self, personagem):
        self.personagem = personagem

    def sortear_recompensa(self):
        # Definição de recompensas possíveis
        recompensas = [
            {"tipo": "ouro", "quantidade": random.randint(10, 50)},
            {"tipo": "experiencia", "quantidade": random.randint(20, 100)},
            {"tipo": "item", "nome": "Poção de Vida", "descricao": "Restaura 50 pontos de vida."},
            {"tipo": "item", "nome": "Poção de Mana", "descricao": "Restaura 30 pontos de mana."}
        ]

        # Sorteio da recompensa
        recompensa = random.choice(recompensas)

        # Entregar recompensa ao personagem (se aplicável)
        if recompensa["tipo"] == "ouro":
            mensagem = self.personagem.ganhar_ouro(recompensa["quantidade"])
        elif recompensa["tipo"] == "experiencia":
            mensagem = self.personagem.ganhar_experiencia(recompensa["quantidade"])
        else:
            mensagem = f"{self.personagem.nome} recebeu o item: {recompensa['nome']} - {recompensa['descricao']}"

        return mensagem
