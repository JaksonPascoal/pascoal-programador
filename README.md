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

## Instalação e Execução

> Requer Python 3.10+ e pip atualizado:
```bash
python -m pip install --upgrade pip

1) Clonar o repositório

git clone https://github.com/JaksonPascoal/pascoal-programador.git
cd pascoal-programador

2) Criar e ativar o ambiente virtual

# (opcional, mas recomendado)
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate

3) Instalar dependências e o pacote

pip install -r requirements.txt
pip install -e .   # instala o pacote local em modo editável

4) Executar os testes

pytest -q

5) Iniciar a aplicação web

streamlit run app.py

CLI — exemplos

# Normalizar um texto
python -m pasqalib.cli --norm "  AGUA   E   VIDA  "

# Contar palavras
python -m pasqalib.cli --wc "Ola, mundo! Isto e um teste"

# Gerar Fibonacci
python -m pasqalib.cli --fib 12

# Testar primo e próximo primo
python -m pasqalib.cli --prime 97
python -m pasqalib.cli --next-prime 14

# Conceito da nota
python -m pasqalib.cli --grade 95

📂 Estrutura do Projeto

.
├── app.py                     # Aplicação web (Streamlit)
├── requirements.txt           # Dependências
├── pyproject.toml             # Metadados do pacote
├── src/
│   └── pasqalib/
│       ├── __init__.py
│       ├── cli.py            # CLI (argparse)
│       └── utils.py          # Funções utilitárias
└── tests/
    └── test_utils.py         # Testes com pytest

🧠 Lições Aprendidas

Reprodutibilidade: venv + requirements garantem ambiente limpo.

Qualidade: testes com pytest evitam regressões.

Automação: CLI para rodar rotinas por terminal/servidor.

Produto: Streamlit expõe as funções em interface web.

Pré-processamento de texto: normalize_text e count_words (NLP/ETL).

📄 Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para detalhes.

