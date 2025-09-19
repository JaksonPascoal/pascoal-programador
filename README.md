# Python Project Template: CLI, Tests & Streamlit

[![CI](https://github.com/JaksonPascoal/pascoal-programador/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/JaksonPascoal/pascoal-programador/actions/workflows/tests.yml)

Projeto didático focado em programação, testes e desenvolvimento web para explorar rotinas úteis de Data Science.
É o primeiro bloco do estudo, cobrindo conceitos essenciais de Python e sua aplicação em um produto simples (CLI + App Web).

📝 Sumário

. Funcionalidades

. Tecnologias

. Como Rodar

. Estrutura do Projeto

. Lições Aprendidas

✨ Funcionalidades

O projeto tem três faces: um pacote Python, uma CLI e um App Web.

-Pacote Python (pasqalib)

-Texto / NLP básica

-normalize_text(s) — deixa minúsculo, remove acentos e colapsa espaços.

-count_words(s) — conta palavras após normalizar.

-count_chars(s) — conta caracteres alfanuméricos (útil para limpeza).

-word_freqs(s, top=None) — dicionário com frequência de palavras (normaliza e ignora pontuação; top opcional para top-N).

Números / Algoritmos

-fibonacci(n), fibonacci_list(n)

-is_prime(n), next_prime(n)

Análise de Dados / Estatística (🆕 v0.3.0)

-stats_summary(numbers) — estatísticas descritivas completas (média, mediana, moda, desvio padrão, quartis)

-detect_outliers(numbers, method) — detecta outliers usando IQR ou Z-Score

-correlation_pearson(x, y) — correlação de Pearson entre duas séries

Regras de Negócio

-parse_grade(score) — converte nota 0–100 em conceito A+/A/B/C/D/F.

CLI (Interface de Linha de Comando)

Instalar em modo editável cria o comando pasqa.

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

    # 🆕 Novos comandos v0.3.0 - Análise de Dados
    pasqa --stats "1,2,3,4,5,6,7,8,9,10"                # estatísticas descritivas
    pasqa --outliers "1,2,3,4,5,100" --method iqr       # detecção de outliers (IQR)
    pasqa --outliers "1,2,3,4,5,100" --method zscore    # detecção de outliers (Z-Score)
    pasqa --corr "1,2,3,4,5;2,4,6,8,10"                 # correlação entre séries

Dica: também funciona via módulo:

    python -m pasqalib.cli --help
    
    # Exemplos com módulo (útil para desenvolvimento)
    python -c "import sys; sys.path.insert(0, './src'); from pasqalib.cli import main; main()" --stats "1,2,3,4,5"

App Web (Streamlit)

-Texto: normaliza e conta palavras (com visualização das Top-N frequências).

-Números: sequência de Fibonacci e teste/próximo primo.

-Notas: conceito a partir da nota.

Clean CSV:

-Faz upload de CSV;

-Processa uma coluna de texto (normalização + contagem por linha);

-Gera frequências agregadas da coluna (exibe Top 20 + download do CSV processado).

🛠️ Tecnologias

-Python 3.11+

-pytest (testes)

-streamlit (aplicação web)

-pandas (manipulação de dados)

-CI (GitHub Actions): roda pytest a cada push/PR (badge no topo).

-Formatação/checagens rápidas são feitas localmente com pre-commit.

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
   
# exemplos rápidos:
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
                └── tests.yml               # CI: pytest em cada push/PR


🧠 Aprendizado

Reprodutibilidade — venv + requirements garantem ambiente limpo.

Qualidade — testes com pytest evitam regressões ao evoluir código.

Automação — CLI facilita rodar rotinas em terminal/servidor.

Produto — Streamlit expõe as funções em interface amigável.

Pré-processamento de texto — normalize_text, count_words, word_freqs (NLP/ETL).

CI/CD básico — GitHub Actions valida o projeto a cada PR/push.

📄 Licença

Este projeto está licenciado sob a MIT License.
Veja o arquivo LICENSE para mais detalhes.









 
