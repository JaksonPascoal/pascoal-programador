import streamlit as st
import pandas as pd
from pasqalib.utils import (
    normalize_text, count_words,
    fibonacci, fibonacci_list,
    is_prime, next_prime, parse_grade
)

# 1ª chamada Streamlit
st.set_page_config(page_title="Pascoal • Bloco 1", page_icon="📊", layout="centered")

st.title("Bloco 1 — App Web (Pascoal)")
st.caption("JkPascoal")

tabs = st.tabs(["📝 Texto", "🔢 Números", "🏷️ Notas", "🧼 Clean CSV"])

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

# --- Clean CSV ---
with tabs[3]:
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

        new_name = st.text_input(
            "Nome da coluna normalizada (se aplicável):",
            value=f"{col_sel}_norm"
        )

        if st.button("Limpar e gerar CSV"):
            df_out = df.copy()
            source_series = df_out[col_sel]

            if do_norm:
                df_out[new_name] = source_series.astype("string").apply(normalize_text)
                base_for_count = df_out[new_name]
            else:
                base_for_count = source_series.astype("string")

            if do_wc:
                df_out[f"{col_sel}_wc"] = base_for_count.apply(count_words)

            st.success("Processado! Prévia:")
            st.dataframe(df_out.head(10), use_container_width=True)

            csv_bytes = df_out.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="⬇️ Baixar CSV processado",
                data=csv_bytes,
                file_name="csv_processado.csv",
                mime="text/csv",
            )
    else:
        st.info("Envie um CSV para começar.")
