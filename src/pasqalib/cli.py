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


if __name__ == "__main__":
    main()
