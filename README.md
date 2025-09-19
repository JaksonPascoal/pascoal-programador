# PascoalLib: Sistema Completo de Análise de Dados 📊

[![CI](https://github.com/Jk-Pascoal/pascoal-programador/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/Jk-Pascoal/pascoal-programador/actions/workflows/tests.yml)
[![Version](https://img.shields.io/badge/version-0.3.0-blue.svg)](https://github.com/Jk-Pascoal/pascoal-programador/releases)
[![Python](https://img.shields.io/badge/python-3.11+-brightgreen.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

> **Sistema completo de análise de dados** com processamento de texto, algoritmos matemáticos e análise estatística avançada. Oferece múltiplas interfaces: pacote Python, CLI e aplicação web interativa.

## � Sumário

- [✨ Funcionalidades](#-funcionalidades)
- [🛠️ Tecnologias](#️-tecnologias)  
- [🚀 Como Rodar](#-como-rodar)
- [📂 Estrutura do Projeto](#-estrutura-do-projeto)
- [🎯 Exemplos Avançados](#-exemplos-avançados)
- [🧠 Aprendizado](#-aprendizado)
- [📄 Licença](#-licença)

## ✨ Funcionalidades

### 📦 **Pacote Python (pasqalib)**

#### **📝 Processamento de Texto / NLP:**
- `normalize_text(s)` — Normalização completa (minúsculas, remove acentos, colapsa espaços)
- `count_words(s)` — Contagem de palavras após normalização
- `count_chars(s)` — Contagem de caracteres alfanuméricos (útil para limpeza)
- `word_freqs(s, top=None)` — Análise de frequência de palavras com opção top-N

#### **🔢 Algoritmos Matemáticos:**
- `fibonacci(n)`, `fibonacci_list(n)` — Sequência de Fibonacci
- `is_prime(n)`, `next_prime(n)` — Testes de primalidade e próximo primo

#### **📊 Análise Estatística (🆕 v0.3.0):**
- `stats_summary(numbers)` — Estatísticas descritivas completas (média, mediana, desvio padrão, quartis)
- `detect_outliers(numbers, method)` — Detecção de outliers usando métodos IQR ou Z-Score
- `correlation_pearson(x, y)` — Correlação de Pearson entre duas séries com significância

#### **🎓 Regras de Negócio:**
- `parse_grade(score)` — Conversão de notas 0-100 para conceitos A+/A/B/C/D/F

### 🖥️ **CLI (Interface de Linha de Comando)**

Instalar em modo editável cria o comando `pasqa`:

```bash
pasqa --help
```

#### **Exemplos de Uso:**

```bash
# Processamento de Texto
pasqa --norm "  ÁGUA   É   VIDA  "
pasqa --wc "Olá, mundo! Isto é um teste"
pasqa --cc "Água é vida!"
pasqa --freq "Olá, olá! água é vida. Água!"         # dicionário de frequências
pasqa --freq "Olá, olá! água é vida. Água!" --top 3 # top-N frequências

# Algoritmos Matemáticos
pasqa --fib 12
pasqa --prime 97
pasqa --next-prime 14
pasqa --grade 95

# 🆕 Análise Estatística (v0.3.0)
pasqa --stats "1,2,3,4,5,6,7,8,9,10"                # estatísticas descritivas
pasqa --outliers "1,2,3,4,5,100" --method iqr       # detecção de outliers (IQR)
pasqa --outliers "1,2,3,4,5,100" --method zscore    # detecção de outliers (Z-Score)
pasqa --corr "1,2,3,4,5;2,4,6,8,10"                 # correlação entre séries
```

**Dica:** Também funciona via módulo para desenvolvimento:
```bash
python -m pasqalib.cli --help
python -c "import sys; sys.path.insert(0, './src'); from pasqalib.cli import main; main()" --stats "1,2,3,4,5"
```

### 🌐 **App Web (Streamlit)**

Interface web interativa com **5 abas funcionais**:

#### **📝 Aba Texto:**
- Normalização e contagem de palavras
- Visualização de frequências Top-N
- Análise de caracteres alfanuméricos

#### **🔢 Aba Números:**
- Sequência de Fibonacci interativa
- Teste de primalidade
- Busca do próximo primo

#### **🎓 Aba Notas:**
- Conversão de notas para conceitos
- Validação de entrada
- Escala de avaliação automática

#### **🧹 Aba Clean CSV:**
- Upload de arquivos CSV
- Processamento de colunas de texto
- Normalização e contagem por linha
- Frequências agregadas (Top 20)
- Download de dados processados

#### **📊 🆕 Aba Análise de Dados (v0.3.0):**
- **Upload de datasets CSV** com detecção automática de separador
- **Estatísticas descritivas automáticas** (média, mediana, desvio padrão, quartis)
- **Detecção visual de outliers** com métodos IQR e Z-Score
- **Matriz de correlação interativa** com heatmap colorido
- **Gráficos de distribuição** e dispersão
- **Visualizações com Plotly** totalmente interativas
- **Download de dados** processados e análises

## 🛠️ Tecnologias

### **Core Stack:**
- **Python 3.11+** — Versão moderna com recursos avançados
- **pytest** — Framework de testes unitários robusto
- **streamlit** — Aplicação web interativa e moderna
- **pandas** — Manipulação e análise de dados

### **🆕 Análise Estatística (v0.3.0):**
- **scipy** — Funções estatísticas avançadas e científicas
- **plotly** — Visualizações interativas e dashboards
- **openpyxl** — Suporte completo a arquivos Excel

### **DevOps & Qualidade:**
- **GitHub Actions** — CI/CD automático (pytest em cada push/PR)
- **pre-commit** — Formatação e checagens automáticas
- **pyproject.toml** — Configuração moderna de projeto
- **type hints** — Tipagem estática para melhor código

## 🚀 Como Rodar

### **1. Clonar o repositório:**
```bash
git clone https://github.com/Jk-Pascoal/pascoal-programador.git
cd pascoal-programador
```

### **2. Criar ambiente virtual (recomendado):**
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate
```

### **3. Instalar dependências:**
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install -e .
```

### **4. Executar testes:**
```bash
pytest -q
```

### **5. Iniciar aplicação web:**
```bash
# Versão desenvolvimento
streamlit run app.py

# 🆕 Versão para deploy (v0.3.0)
streamlit run app_standalone.py
```

*💡 A versão standalone não depende do pacote instalado - ideal para deploy em nuvem*

### **6. Usar CLI:**
```bash
pasqa --help

# Exemplos rápidos
pasqa --norm "  ÁGUA   É   VIDA  "
pasqa --freq "Olá, olá! água é vida. Água!" --top 5
pasqa --stats "1,2,3,4,5" --method iqr
```

## 📂 Estrutura do Projeto

```
.
├── app.py                          # Aplicação web principal (Streamlit)
├── app_standalone.py               # 🆕 Versão standalone para deploy
├── requirements.txt                # Dependências principais
├── requirements_deploy.txt         # 🆕 Dependências mínimas para deploy
├── pyproject.toml                  # Configuração moderna do projeto
├── DEPLOY.md                       # 🆕 Guia completo de deployment
├── CHANGELOG.md                    # 🆕 Histórico detalhado de versões
├── ANALISE_PROJETO.md              # 🆕 Análise técnica completa
├── src/
│   └── pasqalib/
│       ├── __init__.py             # Inicialização do pacote
│       ├── cli.py                  # CLI + comandos estatísticos
│       └── utils.py                # Funções core (texto/math/stats)
├── tests/
│   └── test_utils.py               # Testes unitários abrangentes
├── .streamlit/
│   └── config.toml                 # 🆕 Configuração Streamlit
└── .github/
    └── workflows/
        └── tests.yml               # CI/CD automático
```

## 🎯 Exemplos Avançados v0.3.0

### **📊 Análise Estatística via CLI:**

```bash
# Dataset de vendas mensais
pasqa --stats "1200,1350,1180,1420,1390,1250,1600,1550,1480,1320,1290,1450"

# Detectar meses com vendas anômalas  
pasqa --outliers "1200,1350,1180,1420,1390,1250,2800,1550,1480,1320,1290,1450" --method iqr

# Correlação entre temperatura e vendas de sorvete
pasqa --corr "25,28,32,30,35,38,40,42,38,35,30,28;120,135,180,142,195,250,280,300,245,200,150,130"
```

### **🌐 Casos de Uso Web (Streamlit):**

- **📈 Análise de Datasets:** Upload CSV de vendas, análise automática de outliers
- **🔗 Correlações:** Verificar relação entre variáveis (preço vs demanda, idade vs renda)  
- **🧹 Limpeza de Texto:** Processar comentários de clientes, extrair palavras-chave
- **📊 Dashboard Estatístico:** Visualizar distribuições, identificar padrões anômalos

### **🚀 Deploy Rápido:**

```bash
# Testar localmente
streamlit run app_standalone.py

# Deploy em plataformas como:
# - Streamlit Cloud
# - Heroku  
# - Railway
# - Render

# Usar requirements_deploy.txt para dependências mínimas
```

## 🧠 Aprendizado

### **🔄 Conceitos Fundamentais:**
- **Reprodutibilidade:** `venv` + `requirements.txt` garantem ambiente limpo
- **Qualidade:** Testes com `pytest` evitam regressões ao evoluir código
- **Automação:** CLI facilita execução de rotinas em terminal/servidor
- **Produto:** Streamlit expõe funcionalidades em interface amigável

### **📝 Processamento de Dados:**
- **Pré-processamento de texto:** `normalize_text`, `count_words`, `word_freqs` (NLP/ETL)
- **🆕 Análise Estatística:** `stats_summary`, `detect_outliers`, `correlation_pearson` (Data Science)
- **🆕 Visualização de Dados:** Plotly para gráficos interativos e análise exploratória

### **� DevOps & Deploy:**
- **🆕 Deploy Facilitado:** Versão standalone e guias para implantação em nuvem
- **CI/CD Básico:** GitHub Actions valida projeto a cada PR/push
- **Versionamento:** Tags semânticas e changelog organizado

### **💼 Habilidades Profissionais:**
- **Arquitetura Limpa:** Separação clara entre lógica, CLI e interface
- **Múltiplas Interfaces:** Mesmo core acessível via pacote, CLI e web
- **Documentação Completa:** README, CHANGELOG, guias de deploy
- **Evolução Iterativa:** Roadmap v0.1 → v0.2 → v0.3.0

## �📄 Licença

Este projeto está licenciado sob a MIT License.
Veja o arquivo LICENSE para mais detalhes.
