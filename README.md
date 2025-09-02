# Pascoal • Bloco 1 — Fundamentos de Programação + App Web

[![CI](https://github.com/JaksonPascoal/pascoal-programador/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/JaksonPascoal/pascoal-programador/actions/workflows/tests.yml)


Pequeno projeto didático para treinar **programação + testes + app web** focado em rotinas úteis de Data Science.

## O que tem aqui
- **Pacote Python** `pasqalib` (layout `src/`) com funções:
  - `normalize_text`, `count_words` (limpeza/contagem de texto)
  - `fibonacci`, `fibonacci_list` (lógica/loops)
  - `is_prime`, `next_prime` (algoritmos)
  - `parse_grade` (regras de negócio)
- **Testes** com `pytest`
- **CLI**: `python -m pasqalib.cli --help`
- **App Web (Streamlit)** com abas:
  - **Texto**: normaliza e conta palavras
  - **Números**: Fibonacci e primos
  - **Notas**: conceito A+/A/B/C/D/F
  - **Clean CSV**: envia CSV, normaliza coluna de texto, gera contagem de palavras e permite **download** do CSV processado

## Pré-requisitos
- Python 3.10+ recomendado
- pip atualizado (`python -m pip install --upgrade pip`)

## Como rodar
```bash
# (opcional) ambiente virtual
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate

pip install -r requirements.txt
pip install -e .      # instala o pacote em modo editável
pytest -q             # roda os testes

# App web
streamlit run app.py

CLI — exemplos

python -m pasqalib.cli --norm "  ÁGUA   É   VIDA  "
python -m pasqalib.cli --wc "Olá, mundo! Isto é um teste"
python -m pasqalib.cli --fib 12
python -m pasqalib.cli --prime 97
python -m pasqalib.cli --next-prime 14
python -m pasqalib.cli --grade 95

Estrutura

.
├── app.py
├── requirements.txt
├── pyproject.toml
├── src/
│   └── pasqalib/
│       ├── __init__.py
│       ├── cli.py
│       └── utils.py
└── tests/
    └── test_utils.py

O que aprendi / por que importa (para DS)

Reprodutibilidade (venv + pacotes)

Qualidade (pytest)

Automação (CLI)

Produto (Streamlit)

Pré-processamento de texto (rotina comum em NLP/ETL)

.gitignore (coloque este conteúdo no arquivo .gitignore)

.venv/
__pycache__/
*.pyc
.pytest_cache/
dist/
build/
*.egg-info/
.streamlit/


---

## `requirements.txt` (confira)
Ele deve conter:

pytest>=8.0
streamlit
pandas
