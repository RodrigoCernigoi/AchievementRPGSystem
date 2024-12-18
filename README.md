# Sistema de Tarefas RPG

Este projeto é um sistema de tarefas baseado em RPG, desenvolvido em Python utilizando a biblioteca **Flet** para criar uma interface gráfica interativa. O sistema permite que o usuário crie um personagem, gerencie tarefas (primárias, em progresso e concluídas), e receba recompensas simuladas, como ouro e experiência, ao completar tarefas.

---

## Funcionalidades

- **Criação de Personagem**: O usuário pode criar um personagem, fornecendo um nome e uma classe.
- **Gestão de Tarefas**:
  - Adicionar e visualizar tarefas classificadas como:
    - **Tarefas Primárias**
    - **Tarefas em Progresso**
    - **Tarefas Concluídas**
  - Detalhar cada tarefa, incluindo descrição, dificuldade e recompensas.
  - Alterar o status da tarefa para "Concluída".
- **Interface com Animações**:
  - Animações como "fade in" e "deslizamento" ao transitar entre telas e abas.
- **Sistema de Persistência**:
  - Dados do personagem e tarefas são armazenados em um arquivo JSON para persistência.

---

## Requisitos

- **Python 3.10+**
- **Flet 0.8.0+**
- **Dependências adicionais**:
  - Módulos personalizados: `personagem`, `tarefa`, `gacha`, `file_manager`
- Sistema com suporte a `pt_BR.UTF-8` (Linux ou similar).

---

## Como Instalar

1. **Clone o Repositório**:
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd nome-do-repositorio
   ```

2. **Crie um Ambiente Virtual**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # Linux/Mac
   .venv\Scripts\activate   # Windows
   ```

3. **Instale as Dependências**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Certifique-se de que o Locale Está Configurado** (Linux):
   ```bash
   sudo locale-gen pt_BR.UTF-8
   sudo update-locale LANG=pt_BR.UTF-8
   ```

---

## Como Usar

1. **Execute o Sistema**:
   ```bash
   python main.py
   ```

2. **Funcionalidades Disponíveis**:
   - Criar um personagem com nome e classe.
   - Gerenciar tarefas utilizando abas:
     - Tarefas Primárias
     - Tarefas em Progresso
     - Tarefas Concluídas
   - Concluir tarefas e visualizar recompensas.

3. **Encerrar o Programa**:
   - Use o botão "Sair" para fechar a aplicação.

---

## Estrutura do Projeto

```plaintext
AchievementSystem/
├── data/
│   └── dados_rpg.json  # Arquivo para salvar os dados persistidos
├── modules/
│   ├── personagem.py   # Classe para gerenciamento do personagem
│   ├── tarefa.py       # Classe para tarefas
│   ├── gacha.py        # Sistema de gacha (futuro)
│   └── file_manager.py # Funções para salvar/carregar dados
├── main.py             # Arquivo principal da aplicação
├── README.md           # Documentação do projeto
└── requirements.txt    # Dependências do projeto
```

---

## Possíveis Problemas

### Erro de Locale
- **Mensagem**: `'FlutterEngineUpdateLocales' returned 'kInvalidArguments'`
- **Solução**:
  - Verifique se o sistema possui `pt_BR.UTF-8` configurado corretamente.
  - Execute o script com as variáveis de ambiente configuradas:
    ```bash
    LANG=pt_BR.UTF-8 LC_ALL=pt_BR.UTF-8 python main.py
    ```

### Depreciações no Flet
- **Mensagem**: `colors enum is deprecated`
- **Solução**:
  - Atualize o código para usar `Colors` em vez de `colors`.

---

## Melhorias Futuras

- Adicionar sistema de gacha para recompensas aleatórias.
- Implementar níveis e habilidades para o personagem.
- Melhorar a interface com mais animações e temas personalizáveis.
- Criar suporte para múltiplos idiomas.

---

## Contribuições

Sinta-se à vontade para enviar issues ou pull requests no repositório para melhorias ou correções.

---

## Licença

Este projeto é distribuído sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

---

**Desenvolvido com ❤️ por [Darkizu](https://github.com/seu-usuario)**

