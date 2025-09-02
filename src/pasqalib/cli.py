import argparse
from .utils import normalize_text, fibonacci, is_prime, parse_grade, count_words, next_prime

def main():
    parser = argparse.ArgumentParser(description="Kata CLI — Bloco 1")
    parser.add_argument("--norm", help="Normaliza um texto", type=str)
    parser.add_argument("--fib", help="n-ésimo Fibonacci (n>=0)", type=int)
    parser.add_argument("--prime", help="Testa se n é primo", type=int)
    parser.add_argument("--grade", help="Converte nota (0-100) para conceito A+/A/B/C/D/F", type=int)
    parser.add_argument("--wc", help="Conta palavras do texto", type=str)
    parser.add_argument("--next-prime", help="Menor primo >= n", type=int)
    args = parser.parse_args()

    if args.next_prime is not None:
        print(next_prime(args.next_prime))
    if args.wc is not None:
        print(count_words(args.wc))
    if args.norm is not None:
        print(normalize_text(args.norm))
    if args.fib is not None:
        print(fibonacci(args.fib))
    if args.prime is not None:
        print(is_prime(args.prime))
    if args.grade is not None:
        print(parse_grade(args.grade))

if __name__ == "__main__":
    main()


