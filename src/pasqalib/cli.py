import argparse
import json

from .utils import (
    count_chars,
    count_words,
    fibonacci,
    is_prime,
    next_prime,
    normalize_text,
    parse_grade,
    word_freqs,
    stats_summary,
    detect_outliers,
    correlation_pearson,
)


def main():
    parser = argparse.ArgumentParser(description="Kata CLI — Bloco 1")

    # Texto
    parser.add_argument("--norm", type=str, help="Normaliza um texto")
    parser.add_argument("--wc", type=str, help="Conta palavras do texto")
    parser.add_argument("--cc", type=str, help="Conta caracteres alfanuméricos do texto")
    parser.add_argument(
        "--freq",
        type=str,
        help="Frequência de palavras (normaliza, remove pontuação e agrega)",
    )
    parser.add_argument(
        "--top",
        type=int,
        default=0,
        help="Limita ao Top-N (usar junto com --freq; 0 = todos)",
    )

    # Números
    parser.add_argument("--fib", type=int, help="n-ésimo Fibonacci (n>=0)")
    parser.add_argument("--prime", type=int, help="Testa se é primo")
    parser.add_argument("--next-prime", type=int, help="Menor primo ≥ n")

    # Notas
    parser.add_argument("--grade", type=int, help="Converte nota (0–100) para conceito A+/A/B/C/D/F")

    # Estatísticas
    parser.add_argument("--stats", type=str, help="Estatísticas descritivas de números (formato: '1,2,3,4,5')")
    parser.add_argument("--outliers", type=str, help="Detecta outliers (formato: '1,2,3,4,5')")
    parser.add_argument("--method", type=str, default="iqr", choices=["iqr", "zscore"], 
                       help="Método de detecção de outliers (usar com --outliers)")
    parser.add_argument("--corr", type=str, help="Correlação entre duas séries (formato: 'x1,x2,x3;y1,y2,y3')")

    args = parser.parse_args()

    # --- Texto ---
    if args.norm is not None:
        print(normalize_text(args.norm))

    if args.wc is not None:
        print(count_words(args.wc))

    if args.cc is not None:
        print(count_chars(args.cc))

    if args.freq is not None:
        freqs = word_freqs(args.freq)  # já normaliza e remove pontuação
        if args.top and args.top > 0:
            # ordena por frequência desc, depois alfabético
            top_items = sorted(freqs.items(), key=lambda kv: (-kv[1], kv[0]))[: args.top]
            print(json.dumps(dict(top_items), ensure_ascii=False))
        else:
            print(json.dumps(freqs, ensure_ascii=False))

    # --- Números ---
    if args.fib is not None:
        print(fibonacci(args.fib))

    if args.prime is not None:
        print(is_prime(args.prime))

    if args.next_prime is not None:
        print(next_prime(args.next_prime))

    # --- Notas ---
    if args.grade is not None:
        print(parse_grade(args.grade))

    # --- Estatísticas ---
    if args.stats is not None:
        try:
            numbers = [float(x.strip()) for x in args.stats.split(",")]
            stats = stats_summary(numbers)
            print(json.dumps(stats, ensure_ascii=False))
        except ValueError as e:
            print(f"Erro: {e}")

    if args.outliers is not None:
        try:
            numbers = [float(x.strip()) for x in args.outliers.split(",")]
            outliers_info = detect_outliers(numbers, method=args.method)
            print(json.dumps(outliers_info, ensure_ascii=False))
        except ValueError as e:
            print(f"Erro: {e}")

    if args.corr is not None:
        try:
            x_str, y_str = args.corr.split(";")
            x = [float(i.strip()) for i in x_str.split(",")]
            y = [float(i.strip()) for i in y_str.split(",")]
            corr = correlation_pearson(x, y)
            print(f"Correlação de Pearson: {corr}")
        except ValueError as e:
            print(f"Erro: {e}")


if __name__ == "__main__":
    main()
