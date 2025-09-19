import pytest

from pasqalib.utils import (
    count_chars,
    count_words,
    fibonacci,
    fibonacci_list,
    is_prime,
    next_prime,
    normalize_text,
    parse_grade,
    word_freqs,
    stats_summary,
    detect_outliers,
    correlation_pearson,
)


def test_normalize_text():
    assert normalize_text("  Olá,   MUNDO!  ") == "ola, mundo!"
    assert normalize_text(None) == ""

def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(7) == 13
    with pytest.raises(ValueError):
        fibonacci(-1)

def test_is_prime():
    assert not is_prime(0)
    assert not is_prime(1)
    assert is_prime(2)
    assert is_prime(13)
    assert not is_prime(21)


def test_parse_grade():
    assert parse_grade(95) == "A+"   # novo A+
    assert parse_grade(90) == "A"    # garante A sem '+'
    assert parse_grade(85) == "B"
    assert parse_grade(72) == "C"
    assert parse_grade(65) == "D"
    assert parse_grade(59) == "F"


def test_count_words():
    assert count_words("") == 0
    assert count_words("   ") == 0
    assert count_words("Olá, mundo!") == 2
    assert count_words("  Olá,   mundo!  Isto é   um teste ") == 6

def test_fibonacci_list():
    assert fibonacci_list(0) == [0]
    assert fibonacci_list(1) == [0, 1]
    assert fibonacci_list(5) == [0, 1, 1, 2, 3, 5]

def test_next_prime():
    assert next_prime(0) == 2
    assert next_prime(2) == 2
    assert next_prime(14) == 17
    assert next_prime(97) == 97

def test_count_chars():
    assert count_chars("") == 0
    assert count_chars("Olá!") == 3      # "ola!" -> o,l,a
    assert count_chars("A1 B2") == 4     # A,1,B,2
    assert count_chars("  ÁGUA   É   VIDA  ") == 9  # "agua e vida" -> 9

def test_word_freqs():
    assert word_freqs("") == {}
    assert word_freqs("Olá, olá!") == {"ola": 2}
    assert word_freqs("Água é vida. Água!") == {"agua": 2, "e": 1, "vida": 1}


def test_stats_summary():
    numbers = [1, 2, 3, 4, 5]
    stats = stats_summary(numbers)
    assert stats["mean"] == 3.0
    assert stats["median"] == 3
    assert stats["min"] == 1
    assert stats["max"] == 5
    assert stats["count"] == 5
    
    # Teste com lista vazia
    with pytest.raises(ValueError):
        stats_summary([])


def test_detect_outliers():
    # Dados com outliers óbvios
    numbers = [1, 2, 3, 4, 5, 100]  # 100 é outlier
    
    # Teste IQR
    outliers_iqr = detect_outliers(numbers, method="iqr")
    assert outliers_iqr["method"] == "IQR"
    assert 100 in outliers_iqr["outliers"]
    
    # Teste Z-score
    outliers_zscore = detect_outliers(numbers, method="zscore")
    assert outliers_zscore["method"] == "Z-Score"
    
    # Teste com método inválido
    with pytest.raises(ValueError):
        detect_outliers(numbers, method="invalid")


def test_correlation_pearson():
    # Correlação perfeita positiva
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]
    assert correlation_pearson(x, y) == 1.0
    
    # Correlação perfeita negativa
    y_neg = [10, 8, 6, 4, 2]
    assert correlation_pearson(x, y_neg) == -1.0
    
    # Teste com listas de tamanhos diferentes
    with pytest.raises(ValueError):
        correlation_pearson([1, 2], [1, 2, 3])
    
    # Teste com menos de 2 valores
    with pytest.raises(ValueError):
        correlation_pearson([1], [1])

