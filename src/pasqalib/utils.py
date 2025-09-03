"""Utilitários do Bloco 1: limpeza de texto, Fibonacci, primalidade e regras de nota."""

import math
import re
import unicodedata
from collections import Counter


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
    """Retorna a frequência de palavras após normalizar e remover pontuação.
    - Normaliza com `normalize_text`
    - Remove caracteres não alfanuméricos (mantém espaços)
    - Separa por espaços e ignora vazios
    Ex.: "Água é vida. Água!" -> {"agua": 2, "e": 1, "vida": 1}
    """
    s = normalize_text(s)
    if s == "":
        return {}

    # remove tudo que NÃO é a-z, 0-9 ou espaço → vira espaço
    s = re.sub(r"[^a-z0-9\s]+", " ", s)

    tokens = s.split()  # divide por qualquer quantidade de espaços
    return dict(Counter(tokens))
