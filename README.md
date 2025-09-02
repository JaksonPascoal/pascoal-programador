# Pascoal | Fundamentos de Programação + App Web

[![CI](https://github.com/JaksonPascoal/pascoal-programador/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/JaksonPascoal/pascoal-programador/actions/workflows/tests.yml)

Um projeto didático focado em **programação, testes e desenvolvimento web** para explorar rotinas úteis de **Data Science**. Este repositório é o primeiro bloco de um estudo aprofundado, cobrindo conceitos essenciais de Python e sua aplicação em um projeto prático.

---

### 📝 Sumário
- [Funcionalidades](#-funcionalidades)
- [Tecnologias](#-tecnologias)
- [Como Rodar](#-como-rodar)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Lições Aprendidas](#-lições-aprendidas)
- [Licença](#-licença)

---

### ✨ Funcionalidades

O projeto é composto por um pacote Python, uma interface de linha de comando (CLI) e uma aplicação web interativa:

* **Pacote Python (`pasqalib`):**
    * **Limpeza e contagem de texto:** funções `normalize_text` e `count_words`.
    * **Lógica e algoritmos:** `fibonacci`, `fibonacci_list`, `is_prime` e `next_prime`.
    * **Regras de negócio:** `parse_grade` para converter notas em conceitos (A+/A/B/C/D/F).

* **CLI (Interface de Linha de Comando):**
    * `python -m pasqalib.cli --help` para ver todas as opções.

* **App Web (Streamlit):**
    * **Texto:** Normaliza e conta palavras de um texto inserido.
    * **Números:** Gera sequências de Fibonacci e identifica números primos.
    * **Notas:** Converte notas numéricas para conceitos.
    * **Clean CSV:** Permite enviar um arquivo CSV, processar uma coluna de texto (normalizar e contar palavras) e fazer o download do arquivo processado.

---

### 🛠️ Tecnologias

* Python 3.10+
* `pytest` para testes
* `streamlit` para a aplicação web
* `pandas` para manipulação de dados

---

### 🚀 Como Rodar

#### Pré-requisitos
Certifique-se de ter o Python 3.10+ e o `pip` atualizado:
```bash
python -m pip install --upgrade pip

Instalação e Execução

1. Clone o repositório:

git clone [https://github.com/JaksonPascoal/pascoal-programador.git](https://github.com/JaksonPascoal/pascoal-programador.git)
cd pascoal-programador

2. Crie e ative um ambiente virtual:

# (opcional, mas recomendado)
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate

3. Instale as dependências:

pip install -r requirements.txt
pip install -e .  # Instala o pacote local em modo editável

4. Execute os testes:

pytest -q

5. Inicie a aplicação web:

streamlit run app.py

6. Use a CLI:

# Normalizar um texto
python -m pasqalib.cli --norm "  ÁGUA   É   VIDA  "

# Contar palavras
python -m pasqalib.cli --wc "Olá, mundo! Isto é um teste"

# Gerar Fibonacci
python -m pasqalib.cli --fib 12

📂 Estrutura do Projeto

.
├── app.py                     # Aplicação web Streamlit
├── requirements.txt           # Dependências do projeto
├── pyproject.toml             # Configurações do projeto
├── src/                       # Código-fonte principal
│   └── pasqalib/
│       ├── __init__.py
│       ├── cli.py             # Lógica da CLI
│       └── utils.py           # Funções utilitárias
└── tests/
    └── test_utils.py          # Testes com pytest

🧠 Lições Aprendidas
Este projeto serviu como uma base sólida para entender conceitos fundamentais no desenvolvimento de software e Data Science:

Reprodutibilidade: O uso de ambientes virtuais (venv) e o gerenciamento de dependências (requirements.txt) garantem que o projeto possa ser executado em qualquer ambiente sem conflitos.

Qualidade do Código: A prática de escrever testes (pytest) antes ou durante a codificação ajuda a garantir a qualidade, a confiabilidade e a estabilidade do software.

Automação: A criação de uma interface de linha de comando (CLI) demonstra como é possível automatizar tarefas e interagir com o código de forma programática.

Produto: A construção de uma aplicação web interativa (Streamlit) mostra como empacotar e disponibilizar uma funcionalidade como um produto final para usuários não técnicos.

Pré-processamento de Texto: A inclusão de rotinas como normalize_text e count_words é uma prática essencial em pipelines de Processamento de Linguagem Natural (NLP) e ETL (Extract, Transform, Load).

📄 Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.