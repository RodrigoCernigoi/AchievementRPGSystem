import json

def salvar_dados(arquivo, dados):
    """
    Salva os dados em um arquivo JSON.
    """
    try:
        with open(arquivo, 'w', encoding='utf-8') as f:
            json.dump(dados, f, ensure_ascii=False, indent=4)
        return "Dados salvos com sucesso!"
    except Exception as e:
        return f"Erro ao salvar os dados: {e}"

def carregar_dados(arquivo):
    """
    Carrega os dados de um arquivo JSON. Retorna um dicionário ou None se o arquivo não existir.
    """
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return None
    except Exception as e:
        print(f"Erro ao carregar os dados: {e}")
        return None

