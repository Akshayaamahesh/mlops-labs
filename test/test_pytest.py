import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))
import text_utils


def test_word_count():
    assert text_utils.word_count("hello world") == 2
    assert text_utils.word_count("") == 0
    assert text_utils.word_count("  extra   spaces  here ") == 3


def test_reverse_text():
    assert text_utils.reverse_text("abc") == "cba"
    assert text_utils.reverse_text("") == ""


def test_is_palindrome():
    assert text_utils.is_palindrome("racecar") is True
    assert text_utils.is_palindrome("A man, a plan, a canal: Panama") is True
    assert text_utils.is_palindrome("hello") is False


def test_text_summary():
    result = text_utils.text_summary("level up")
    assert result == {
        "word_count": 2,
        "reversed": "pu level",
        "is_palindrome": False,
    }


def test_invalid_input():
    with pytest.raises(ValueError):
        text_utils.word_count(123)


@pytest.mark.parametrize("text, expected", [
    ("madam", True),
    ("Was it a car or a cat I saw", True),
    ("python", False),
])
def test_is_palindrome_parametrized(text, expected):
    assert text_utils.is_palindrome(text) == expected