class Personagem:
    def __init__(self, nome, classe):
        self.nome = nome
        self.classe = classe
        self.nivel = 1
        self.experiencia = 0
        self.ouro = 0

    def ganhar_ouro(self, quantidade):
        self.ouro += quantidade
        return f"{self.nome} recebeu {quantidade} de ouro! Ouro total: {self.ouro}"

    def ganhar_experiencia(self, quantidade):
        self.experiencia += quantidade
        resultado = f"{self.nome} ganhou {quantidade} de EXP! EXP total: {self.experiencia}\n"
        resultado += self.verificar_nivel_up()
        return resultado

    def verificar_nivel_up(self):
        mensagem = ""
        while self.experiencia >= self.nivel * 100:
            self.experiencia -= self.nivel * 100
            self.nivel += 1
            mensagem += f"Parabéns! {self.nome} subiu para o nível {self.nivel}!\n"
        return mensagem

    def to_dict(self):
        return {
            "nome": self.nome,
            "classe": self.classe,
            "nivel": self.nivel,
            "experiencia": self.experiencia,
            "ouro": self.ouro
        }

    @classmethod
    def from_dict(cls, data):
        personagem = cls(data["nome"], data["classe"])
        personagem.nivel = data["nivel"]
        personagem.experiencia = data["experiencia"]
        personagem.ouro = data["ouro"]
        return personagem
