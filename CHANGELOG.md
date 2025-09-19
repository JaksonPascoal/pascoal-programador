# Changelog
Todas as mudanças notáveis deste projeto serão documentadas aqui.

O formato segue **Keep a Changelog** e o versionamento segue **SemVer**.

## [Unreleased]
- (adicione aqui o que entrar **depois** da v0.3.0)

## [0.3.0] - 2025-09-18
### Added
- `stats_summary(numbers)`: Estatísticas descritivas completas (média, mediana, moda, desvio padrão, quartis, range)
- `detect_outliers(numbers, method)`: Detecção de outliers usando métodos IQR ou Z-Score
- `correlation_pearson(x, y)`: Cálculo de correlação de Pearson entre duas séries
- CLI: Novos comandos `--stats`, `--outliers`, `--corr` para análise estatística
- App (Streamlit): Nova aba "📊 Análise de Dados" com:
  - Entrada manual de números ou geração de dados aleatórios
  - Métricas estatísticas interativas
  - Detecção visual de outliers
  - Histograma de distribuição
  - Análise de correlação automática

### Changed
- Versão atualizada para 0.3.0 com foco em análise de dados
- README atualizado com exemplos dos novos comandos CLI
- Estrutura do app Streamlit reorganizada com 5 abas

### Dependencies
- Adicionadas: scipy>=1.11.0, plotly>=5.0.0, openpyxl>=3.1.0 para futuras funcionalidades

### Docs
- Exemplos de uso dos novos comandos CLI no README
- Documentação das novas funções de análise estatística

## [0.2.0] - 2025-09-04
### Added
- `word_freqs(series)`: calcula frequência absoluta e relativa de palavras em uma coluna de texto (pandas Series).
- App (Streamlit): mostra **tabela de frequências** e **gráfico Top-N** na aba **Clean CSV**.

### Changed
- App (Streamlit): seletor de colunas robusto (suporta nomes não-string).  
- Títulos e organização visual do app/README.

### Fixed
- Erro de `selectbox` quando o CSV tinha nomes de colunas numéricos (`int64`).

### Docs
- README atualizado (instruções, funcionalidades e prints do app).
- Docstrings e exemplos nos testes.

### CI/Tooling
- Pre-commit com **ruff** (lint + auto-fix) e **black** (formatação).
- GitHub Actions para rodar **pytest** em push/PR.

## [0.1.0] - 2025-09-02
### Added
- Primeira versão do pacote `pasqalib` com:
  - Texto: `normalize_text`, `count_words`
  - Números: `fibonacci`, `fibonacci_list`, `is_prime`, `next_prime`
  - Regras: `parse_grade` (inclui A+ ≥ 95)
- CLI inicial (`python -m pasqalib.cli`) com comandos para normalizar/contar, fibonacci, primo, próximo primo e conceito.
- App (Streamlit) com abas **Texto**, **Números** e **Notas**.
