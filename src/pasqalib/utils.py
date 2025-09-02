import math
import re
import unicodedata

def normalize_text(s: str) -> str:
    """Minúsculas, sem acentos extra, colapsa espaços."""
    if s is None:
        return ""
    # lower
    s = s.lower()
    # remove diacríticos
    s = unicodedata.normalize("NFKD", s)
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    # troca múltiplos espaços por 1
    s = re.sub(r"\s+", " ", s).strip()
    return s

def fibonacci(n: int) -> int:
    """Retorna F(n). Define F(0)=0, F(1)=1. Uso de laço simples."""
    if n < 0:
        raise ValueError("n deve ser >= 0")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def is_prime(n: int) -> bool:
    """Teste simples de primalidade para n >= 0."""
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    r = int(math.isqrt(n))
    for k in range(3, r+1, 2):
        if n % k == 0:
            return False
    return True

def parse_grade(score: int) -> str:
    """Mapeia 0-100 em conceitos A+/A/B/C/D/F."""
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
    """Conta palavras após normalizar (minúsculas, sem acentos, espaços colapsados)."""
    s = normalize_text(s)
    if s == "":
        return 0
    return len(s.split())

def fibonacci_list(k: int) -> list[int]:
    """Retorna [F(0), F(1), ..., F(k)] (k >= 0)."""
    if k < 0:
        raise ValueError("k deve ser >= 0")
    a, b = 0, 1
    seq = [a]
    for _ in range(k):
        a, b = b, a + b
        seq.append(a)
    return seq

def next_prime(n: int) -> int:
    """Retorna o menor primo >= n."""
    if n <= 2:
        return 2
    x = n if n % 2 else n + 1   # começa no ímpar >= n
    while not is_prime(x):
        x += 2                   # pula só ímpares
    return x


