from pasqalib.utils import normalize_text, fibonacci, is_prime, parse_grade, count_words, fibonacci_list, next_prime, count_chars

import pytest

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
    assert parse_grade(95) == "A"
    assert parse_grade(85) == "B"
    assert parse_grade(75) == "C"
    assert parse_grade(65) == "D"
    assert parse_grade(10) == "F"
    with pytest.raises(ValueError):
        parse_grade(101)

def test_parse_grade():
    assert parse_grade(95) == "A+"   # novo
    assert parse_grade(90) == "A"    # garante A sem o '+'
    assert parse_grade(85) == "B"
    assert parse_grade(75) == "C"
    assert parse_grade(65) == "D"
    assert parse_grade(10) == "F"
    with pytest.raises(ValueError):
        parse_grade(101)

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
