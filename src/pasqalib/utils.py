"""Utilitários do Bloco 1: limpeza de texto, Fibonacci, primalidade e regras de nota."""

import math
import re
import unicodedata
from collections import Counter
from typing import Union


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


def stats_summary(numbers: list[Union[int, float]]) -> dict[str, float]:
    """Calcula estatísticas descritivas de uma lista de números.
    
    Args:
        numbers: Lista de números (int ou float)
    
    Returns:
        Dict com mean, median, mode, std_dev, min, max, q1, q3
    
    Raises:
        ValueError: Se a lista estiver vazia
    """
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
    """Detecta outliers em uma lista de números.
    
    Args:
        numbers: Lista de números
        method: Método de detecção ("iqr" ou "zscore")
    
    Returns:
        Dict com outliers detectados e estatísticas
    """
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
    """Calcula correlação de Pearson entre duas séries.
    
    Args:
        x, y: Listas de números do mesmo tamanho
    
    Returns:
        Coeficiente de correlação (-1 a 1)
    """
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
