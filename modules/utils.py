import time
from datetime import datetime

def animacao_fade_in(mensagem):
    for i in range(1, len(mensagem) + 1):
        print(mensagem[:i], end="\r", flush=True)
        time.sleep(0.05)
    print()

def animacao_fade_out(mensagem):
    for i in range(len(mensagem), 0, -1):
        print(mensagem[:i], end="\r", flush=True)
        time.sleep(0.05)
    print(" " * len(mensagem), end="\r")

def saudacao(nome):
    hora_atual = datetime.now().hour
    if 5 <= hora_atual < 12:
        cumprimento = "Bom dia"
    elif 12 <= hora_atual < 18:
        cumprimento = "Boa tarde"
    else:
        cumprimento = "Boa noite"

    return f"{cumprimento}, {nome}! Bem-vindo ao sistema de tarefas RPG!"

# Exemplo de uso para mensagens interativas
def mostrar_boas_vindas(nome):
    mensagem = saudacao(nome)
    animacao_fade_in(mensagem)
    time.sleep(1)
    animacao_fade_out(mensagem)
