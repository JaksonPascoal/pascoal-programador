import pandas as pd
import streamlit as st
import sys
import os

# Adicionar o diretório src ao path para imports locais
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, 'src')
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)

try:
    from pasqalib.utils import (
        count_words,
        fibonacci,
        fibonacci_list,
        is_prime,
        next_prime,
        normalize_text,  # agora com word_freqs
        parse_grade,
        word_freqs,
        stats_summary,
        detect_outliers,
        correlation_pearson,
    )
except ImportError as e:
    st.error(f"❌ Erro ao importar módulo pasqalib: {e}")
    st.error("Certifique-se de que o pacote está instalado corretamente ou que o código está na estrutura correta.")
    st.stop()

# 1ª chamada Streamlit
st.set_page_config(page_title="Pascoal | Python Project Template", page_icon="📊", layout="centered")
st.title("Python Project Template — CLI, Tests & Streamlit")
st.caption("JkPascoal | v0.3.0 - Data Insights Version")

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
