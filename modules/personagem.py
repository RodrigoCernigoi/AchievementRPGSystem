class Personagem:
    def __init__(self, nome, classe):
        self.nome = nome
        self.classe = classe
        self.nivel = 1
        self.experiencia = 0
        self.ouro = 0
        self.itens = []  # Lista para armazenar itens do personagem

    def adicionar_item(self, item):
        self.itens.append(item)
        return f"{self.nome} obteve o item: {item}!"

    def remover_item(self, item):
        if item in self.itens:
            self.itens.remove(item)
            return f"{self.nome} perdeu o item: {item}."
        return f"Item {item} não encontrado no inventário."

    def listar_itens(self):
        return self.itens

    def to_dict(self):
        return {
            "nome": self.nome,
            "classe": self.classe,
            "nivel": self.nivel,
            "experiencia": self.experiencia,
            "ouro": self.ouro,
            "itens": self.itens
        }

    @classmethod
    def from_dict(cls, data):
        personagem = cls(data["nome"], data["classe"])
        personagem.nivel = data["nivel"]
        personagem.experiencia = data["experiencia"]
        personagem.ouro = data["ouro"]
        personagem.itens = data.get("itens", [])
        return personagem
