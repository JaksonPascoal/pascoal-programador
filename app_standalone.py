"""
Versão standalone do app Streamlit para deploy
Inclui todas as funções necessárias sem dependência de instalação do pacote
"""

import pandas as pd
import streamlit as st
import math
import re
import unicodedata
from collections import Counter
from typing import Union


# === FUNÇÕES UTILITÁRIAS (COPIADAS DE utils.py) ===

def normalize_text(s: str) -> str:
    """Converte para minúsculas, remove acentos e colapsa espaços. Se `s` for None, retorna ""."""
    if s is None:
        return ""
    s = s.lower()
    s = unicodedata.normalize("NFKD", s)
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    s = re.sub(r"\s+", " ", s).strip()
    return s


def fibonacci(n: int) -> int:
    """Retorna F(n) com F(0)=0 e F(1)=1. Lança ValueError para n<0."""
    if n < 0:
        raise ValueError("n deve ser >= 0")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def is_prime(n: int) -> bool:
    """Retorna True se `n` for primo. Usa verificação até ⌊√n⌋ e ignora pares (>2)."""
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    r = int(math.isqrt(n))
    for k in range(3, r + 1, 2):
        if n % k == 0:
            return False
    return True


def parse_grade(score: int) -> str:
    """Mapeia nota 0–100 para A+/A/B/C/D/F. Lança ValueError se fora da faixa."""
    if not (0 <= score <= 100):
        raise ValueError("score deve estar entre 0 e 100")
    if score >= 95:
        return "A+"
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"


def count_words(s: str) -> int:
    """Conta palavras após normalizar (divide por espaços)."""
    s = normalize_text(s)
    if s == "":
        return 0
    return len(s.split())


def fibonacci_list(k: int) -> list[int]:
    """Retorna a sequência [F(0), ..., F(k)]. Lança ValueError para k<0."""
    if k < 0:
        raise ValueError("k deve ser >= 0")
    a, b = 0, 1
    seq = [a]
    for _ in range(k):
        a, b = b, a + b
        seq.append(a)
    return seq


def next_prime(n: int) -> int:
    """Retorna o menor primo ≥ n."""
    if n <= 2:
        return 2
    x = n if n % 2 else n + 1
    while not is_prime(x):
        x += 2
    return x


def count_chars(s: str) -> int:
    """Conta caracteres alfanuméricos após normalizar (letras e dígitos)."""
    s = normalize_text(s)
    return sum(ch.isalnum() for ch in s)


def word_freqs(s: str) -> dict[str, int]:
    """Retorna a frequência de palavras após normalizar e remover pontuação."""
    s = normalize_text(s)
    if s == "":
        return {}
    s = re.sub(r"[^a-z0-9\s]+", " ", s)
    tokens = s.split()
    return dict(Counter(tokens))


def stats_summary(numbers: list[Union[int, float]]) -> dict[str, float]:
    """Calcula estatísticas descritivas de uma lista de números."""
    if not numbers:
        raise ValueError("Lista não pode estar vazia")
    
    n = len(numbers)
    sorted_nums = sorted(numbers)
    
    # Média
    mean = sum(numbers) / n
    
    # Mediana
    if n % 2 == 0:
        median = (sorted_nums[n//2 - 1] + sorted_nums[n//2]) / 2
    else:
        median = sorted_nums[n//2]
    
    # Moda (valor mais frequente)
    freq_count = Counter(numbers)
    max_freq = max(freq_count.values())
    modes = [k for k, v in freq_count.items() if v == max_freq]
    mode = modes[0] if len(modes) == 1 else None
    
    # Desvio padrão
    variance = sum((x - mean) ** 2 for x in numbers) / n
    std_dev = math.sqrt(variance)
    
    # Quartis
    def quartile(data, q):
        index = (len(data) - 1) * q
        if index == int(index):
            return data[int(index)]
        else:
            lower = data[int(index)]
            upper = data[int(index) + 1]
            return lower + (upper - lower) * (index - int(index))
    
    q1 = quartile(sorted_nums, 0.25)
    q3 = quartile(sorted_nums, 0.75)
    
    return {
        "count": n,
        "mean": round(mean, 4),
        "median": median,
        "mode": mode,
        "std_dev": round(std_dev, 4),
        "min": min(numbers),
        "max": max(numbers),
        "q1": q1,
        "q3": q3,
        "range": max(numbers) - min(numbers)
    }


def detect_outliers(numbers: list[Union[int, float]], method: str = "iqr") -> dict:
    """Detecta outliers em uma lista de números."""
    if not numbers:
        raise ValueError("Lista não pode estar vazia")
    
    if method == "iqr":
        stats = stats_summary(numbers)
        q1, q3 = stats["q1"], stats["q3"]
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        
        outliers = [x for x in numbers if x < lower_bound or x > upper_bound]
        
        return {
            "method": "IQR",
            "outliers": outliers,
            "count": len(outliers),
            "lower_bound": round(lower_bound, 4),
            "upper_bound": round(upper_bound, 4),
            "percentage": round(len(outliers) / len(numbers) * 100, 2)
        }
    
    elif method == "zscore":
        stats = stats_summary(numbers)
        mean, std_dev = stats["mean"], stats["std_dev"]
        
        z_scores = [(x - mean) / std_dev for x in numbers]
        outliers = [numbers[i] for i, z in enumerate(z_scores) if abs(z) > 2]
        
        return {
            "method": "Z-Score",
            "outliers": outliers,
            "count": len(outliers),
            "threshold": 2,
            "percentage": round(len(outliers) / len(numbers) * 100, 2)
        }
    
    else:
        raise ValueError("Método deve ser 'iqr' ou 'zscore'")


def correlation_pearson(x: list[Union[int, float]], y: list[Union[int, float]]) -> float:
    """Calcula correlação de Pearson entre duas séries."""
    if len(x) != len(y):
        raise ValueError("As listas devem ter o mesmo tamanho")
    
    if len(x) < 2:
        raise ValueError("Precisam de pelo menos 2 valores")
    
    n = len(x)
    mean_x = sum(x) / n
    mean_y = sum(y) / n
    
    numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
    sum_sq_x = sum((x[i] - mean_x) ** 2 for i in range(n))
    sum_sq_y = sum((y[i] - mean_y) ** 2 for i in range(n))
    
    denominator = math.sqrt(sum_sq_x * sum_sq_y)
    
    if denominator == 0:
        return 0.0
    
    return round(numerator / denominator, 4)


# === APLICAÇÃO STREAMLIT ===

# 1ª chamada Streamlit
st.set_page_config(page_title="Pascoal | Python Project Template", page_icon="📊", layout="centered")
st.title("Python Project Template — CLI, Tests & Streamlit")
st.caption("JkPascoal | v0.3.0 - Standalone Deploy Version")

tabs = st.tabs(["📝 Texto", "🔢 Números", "🏷️ Notas", "📊 Análise de Dados", "🧼 Clean CSV"])

# --- Texto ---
with tabs[0]:
    st.subheader("Normalizar & Contar Palavras")
    txt = st.text_area("Digite um texto:", height=150, placeholder="  ÁGUA   É   VIDA  ")
    if st.button("Processar texto"):
        norm = normalize_text(txt)
        wc = count_words(txt)
        st.write("**Normalizado:**", norm)
        st.write("**Palavras:**", wc)

# --- Números ---
with tabs[1]:
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Fibonacci")
        n = st.number_input("n (F(n))", min_value=0, value=10, step=1)
        st.write("F(n):", fibonacci(int(n)))
        st.caption("Sequência até n:")
        st.code(" ".join(map(str, fibonacci_list(int(n)))))

    with col2:
        st.subheader("Primos")
        p = st.number_input("Número para testar primo", min_value=0, value=97, step=1)
        st.write("É primo?", is_prime(int(p)))
        st.write("Próximo primo ≥ n:", next_prime(int(p)))

# --- Notas ---
with tabs[2]:
    st.subheader("Conceito da Nota")
    score = st.number_input("Nota (0–100)", min_value=0, max_value=100, value=95, step=1)
    st.write("Conceito:", parse_grade(int(score)))

# --- Análise de Dados ---
with tabs[3]:
    st.subheader("📊 Análise Estatística de Dados")
    
    # Input de dados
    st.write("**Entrada de Dados:**")
    col1, col2 = st.columns(2)
    
    with col1:
        # Opção 1: Inserir manualmente
        st.write("*Opção 1: Inserir números*")
        numbers_input = st.text_area(
            "Digite números separados por vírgula:",
            value="1, 2, 3, 4, 5, 6, 7, 8, 9, 10",
            height=100
        )
        
    with col2:
        # Opção 2: Gerar dados aleatórios
        st.write("*Opção 2: Gerar dados aleatórios*")
        n_random = st.number_input("Quantidade de números:", min_value=5, max_value=1000, value=50, step=5)
        if st.button("🎲 Gerar dados aleatórios"):
            import random
            random_numbers = [round(random.uniform(1, 100), 2) for _ in range(n_random)]
            numbers_input = ", ".join(map(str, random_numbers))
            st.rerun()
    
    # Processar dados
    if numbers_input.strip():
        try:
            # Parse dos números
            numbers = [float(x.strip()) for x in numbers_input.replace(',', ' ').split() if x.strip()]
            
            if len(numbers) < 2:
                st.error("⚠️ É necessário pelo menos 2 números para análise.")
            else:
                st.success(f"✅ {len(numbers)} números carregados com sucesso!")
                
                # Visualização dos dados
                st.write("**Dados carregados:**")
                st.write(f"Primeiros 10: {numbers[:10]}")
                if len(numbers) > 10:
                    st.write(f"... e mais {len(numbers) - 10} números")
                
                # Divisor
                st.divider()
                
                # Estatísticas Descritivas
                st.write("**📊 Estatísticas Descritivas:**")
                stats = stats_summary(numbers)
                
                # Métricas em colunas
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.metric("Média", f"{stats['mean']:.2f}")
                    st.metric("Mediana", f"{stats['median']:.2f}")
                with col2:
                    st.metric("Mínimo", f"{stats['min']:.2f}")
                    st.metric("Máximo", f"{stats['max']:.2f}")
                with col3:
                    st.metric("Desvio Padrão", f"{stats['std_dev']:.2f}")
                    st.metric("Range", f"{stats['range']:.2f}")
                with col4:
                    st.metric("Q1 (25%)", f"{stats['q1']:.2f}")
                    st.metric("Q3 (75%)", f"{stats['q3']:.2f}")
                
                # Tabela completa
                with st.expander("📋 Ver todas as estatísticas"):
                    stats_df = pd.DataFrame([stats]).T
                    stats_df.columns = ["Valor"]
                    st.dataframe(stats_df, use_container_width=True)
                
                st.divider()
                
                # Detecção de Outliers
                st.write("**🔍 Detecção de Outliers:**")
                outlier_method = st.selectbox("Método:", ["iqr", "zscore"], index=0)
                
                outliers_info = detect_outliers(numbers, method=outlier_method)
                
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Outliers Detectados", outliers_info["count"])
                    st.metric("Percentual", f"{outliers_info['percentage']:.1f}%")
                
                with col2:
                    if outliers_info["count"] > 0:
                        st.write("**Valores outliers:**")
                        outliers_display = outliers_info["outliers"][:5]  # Mostrar apenas os primeiros 5
                        st.code(str(outliers_display))
                        if len(outliers_info["outliers"]) > 5:
                            st.caption(f"... e mais {len(outliers_info['outliers']) - 5} outliers")
                
                # Mostrar limites
                if outlier_method == "iqr" and outliers_info["count"] > 0:
                    st.write(f"**Limites IQR:** {outliers_info['lower_bound']:.2f} a {outliers_info['upper_bound']:.2f}")
                
                st.divider()
                
                # Histograma simples (usando Streamlit)
                st.write("**📈 Distribuição dos Dados:**")
                hist_data = pd.DataFrame({"valores": numbers})
                st.bar_chart(hist_data["valores"].value_counts().sort_index())
                
                # Análise de Correlação (se houver dados suficientes)
                if len(numbers) >= 10:
                    st.divider()
                    st.write("**🔗 Análise de Correlação:**")
                    st.write("*Correlação com sequência numérica (1, 2, 3, ...)*")
                    
                    sequence = list(range(1, len(numbers) + 1))
                    try:
                        corr = correlation_pearson(numbers, sequence)
                        st.metric("Correlação de Pearson", f"{corr:.4f}")
                        
                        if abs(corr) > 0.7:
                            st.success("📈 Forte correlação detectada!")
                        elif abs(corr) > 0.3:
                            st.info("📊 Correlação moderada")
                        else:
                            st.warning("📉 Correlação fraca")
                    except Exception as e:
                        st.error(f"Erro no cálculo de correlação: {e}")
                
        except ValueError as e:
            st.error(f"❌ Erro ao processar números: {e}")
            st.error("Certifique-se de inserir apenas números separados por vírgula ou espaço.")

# --- Clean CSV ---
with tabs[4]:
    st.subheader("Limpeza de coluna de texto (CSV)")

    up = st.file_uploader("Envie um arquivo .csv", type=["csv"])
    if up is not None:
        # tentar inferir separador
        try:
            df = pd.read_csv(up, sep=None, engine="python")
        except Exception:
            up.seek(0)
            df = pd.read_csv(up)

        st.write("Prévia do CSV:")
        st.dataframe(df.head(10), use_container_width=True)

        # sugerir colunas de texto (object/string) — mas permitir qualquer uma
        text_cols = [
            c for c in df.columns
            if df[c].dtype == "object" or str(df[c].dtype).startswith("string")
        ]

        # Mostrar apenas labels str no selectbox e mapear de volta para o nome original
        cols = list(df.columns)                 # nomes originais (podem ser int64 etc.)
        labels = [str(c) for c in cols]         # o que aparece no selectbox
        default_label = str(text_cols[0]) if text_cols else labels[0]
        try:
            default_index = labels.index(default_label)
        except ValueError:
            default_index = 0

        label_escolhida = st.selectbox(
            "Escolha a coluna de texto para processar:",
            options=labels,
            index=default_index,
        )
        # nome ORIGINAL da coluna selecionada
        col_sel = cols[labels.index(label_escolhida)]

        c1, c2 = st.columns(2)
        with c1:
            do_norm = st.checkbox(
                "Normalizar texto", value=True,
                help="minúsculas, sem acentos, espaços colapsados"
            )
        with c2:
            do_wc = st.checkbox("Adicionar contagem de palavras", value=True)

        # NOVO: opção de frequências agregadas
        do_freqs = st.checkbox("Gerar frequências de palavras (agregado)", value=True)

        new_name = st.text_input(
            "Nome da coluna normalizada (se aplicável):",
            value=f"{col_sel}_norm"
        )

        if st.button("Limpar e gerar CSV"):
            df_out = df.copy()
            source_series = df_out[col_sel]

            if do_norm:
                df_out[new_name] = (
                    source_series.astype("string").fillna("").apply(normalize_text)
                )
                base_for_count = df_out[new_name]
            else:
                base_for_count = source_series.astype("string").fillna("")

            if do_wc:
                df_out[f"{col_sel}_wc"] = base_for_count.apply(count_words)

            st.success("Processado! Prévia do CSV gerado:")
            st.dataframe(df_out.head(10), use_container_width=True)

            # NOVO: frequências de palavras agregadas na coluna
            if do_freqs:
                all_text = " ".join(list(base_for_count))
                freqs = word_freqs(all_text)
                df_freq = (
                    pd.DataFrame(freqs.items(), columns=["palavra", "frequencia"])
                    .sort_values("frequencia", ascending=False)
                    .reset_index(drop=True)
                )
                st.caption("Top 20 palavras:")
                st.dataframe(df_freq.head(20), use_container_width=True)
                st.bar_chart(df_freq.head(20).set_index("palavra")["frequencia"])

                csv_freq = df_freq.to_csv(index=False).encode("utf-8")
                st.download_button(
                    label="⬇️ Baixar frequências (CSV)",
                    data=csv_freq,
                    file_name=f"freq_palavras_{str(col_sel)}.csv",
                    mime="text/csv",
                )

            csv_bytes = df_out.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="⬇️ Baixar CSV processado",
                data=csv_bytes,
                file_name="csv_processado.csv",
                mime="text/csv",
            )
    else:
        st.info("Envie um CSV para começar.")

# === FOOTER ===
st.divider()
st.caption("🚀 Pascoal-Programador v0.3.0 | Template Python completo com CLI, Tests & Streamlit")