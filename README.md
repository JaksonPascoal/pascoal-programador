# Pascoal | Python Project Template: CLI, Tests & Streamlit

Projeto didático focado em programação, testes e desenvolvimento web para explorar rotinas úteis de Data Science. É o primeiro bloco de estudo, cobrindo conceitos essenciais de Python e sua aplicação em um produto simples (CLI + App Web).

📝 Sumário

Funcionalidades

Tecnologias

Como Rodar

Estrutura do Projeto

Lições Aprendidas

Licença

✨ Funcionalidades

O projeto tem três faces: pacote Python, CLI e App Web.

Pacote Python (pasqalib)

Texto / NLP básica

normalize_text(s) — minúsculas, remove acentos, colapsa espaços.

count_words(s) — conta palavras após normalizar.

count_chars(s) — conta caracteres alfanuméricos (útil pra limpeza).

word_freqs(s) — frequência de palavras (normaliza e ignora pontuação).

Números / Algoritmos

fibonacci(n), fibonacci_list(n)

is_prime(n), next_prime(n)

Regras de negócio

parse_grade(score) — converte nota 0–100 em conceito A+/A/B/C/D/F.

CLI (Interface de Linha de Comando)

Instalação em modo editável cria o comando pasqa:

pasqa --help


Exemplos:

pasqa --norm "  ÁGUA   É   VIDA  "
pasqa --wc   "Olá, mundo! Isto é um teste"
pasqa --cc   "Água é vida!"
pasqa --freq "Olá, olá! água é vida. Água!"         # dicionário de frequências
pasqa --freq "Olá, olá! água é vida. Água!" --top 3 # top-N frequências
pasqa --fib 12
pasqa --prime 97
pasqa --next-prime 14
pasqa --grade 95


Dica: se preferir, também funciona via módulo:
python -m pasqalib.cli --help

App Web (Streamlit)

Texto: normaliza e conta palavras.

Números: Fibonacci e primos.

Notas: conceito a partir da nota.

Clean CSV:

Faz upload de CSV;

Processa uma coluna de texto (normalização + contagem por linha);

Gera frequências agregadas da coluna (Top 20 + download);

Permite baixar o CSV processado.

🛠️ Tecnologias

Python 3.11+

pytest (testes)

streamlit (aplicação web)

pandas (manipulação de dados)

CI: GitHub Actions roda lint/format e testes a cada push/PR (badge no topo).

🚀 Como Rodar
1) Clonar o repositório
git clone https://github.com/JaksonPascoal/pascoal-programador.git
cd pascoal-programador

2) (Opcional, recomendado) Criar e ativar o ambiente virtual
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate

3) Instalar dependências e o pacote em modo editável
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install -e .

4) Rodar testes
pytest -q

5) Iniciar a aplicação web
streamlit run app.py

6) Usar a CLI
pasqa --help


Exemplos rápidos:

pasqa --norm "  ÁGUA   É   VIDA  "
pasqa --freq "Olá, olá! água é vida. Água!" --top 5

📂 Estrutura do Projeto
.
├── app.py                          # Aplicação web (Streamlit)
├── requirements.txt                # Dependências
├── pyproject.toml                  # Metadados do pacote + console script `pasqa`
├── src/
│   └── pasqalib/
│       ├── __init__.py
│       ├── cli.py                  # CLI (argparse)
│       └── utils.py                # Funções utilitárias (texto/algoritmos)
├── tests/
│   └── test_utils.py               # Testes com pytest
└── .github/
    └── workflows/
        └── tests.yml               # CI: lint/format + pytest em cada push/PR

🧠 Lições Aprendidas

Reprodutibilidade — venv + requirements garantem ambiente limpo.

Qualidade — testes com pytest evitam regressões ao evoluir código.

Automação — CLI facilita rodar rotinas em terminal/servidor.

Produto — Streamlit expõe as funções em uma interface amigável.

Pré-processamento de texto — normalize_text, count_words, word_freqs (NLP/ETL).

CI/CD básico — GitHub Actions garante padrão de qualidade em cada PR.

📄 Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para detalhes.