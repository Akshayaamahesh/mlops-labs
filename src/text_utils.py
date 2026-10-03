def word_count(text):
    """Returns the number of words in the text."""
    if not isinstance(text, str):
        raise ValueError("Input must be a string.")
    return len(text.split())


def reverse_text(text):
    """Returns the text reversed."""
    if not isinstance(text, str):
        raise ValueError("Input must be a string.")
    return text[::-1]


def is_palindrome(text):
    """Returns True if the text reads the same forwards and backwards,
    ignoring case, spaces, and punctuation."""
    if not isinstance(text, str):
        raise ValueError("Input must be a string.")
    cleaned = "".join(ch for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]


def text_summary(text):
    """Combines the above functions and returns a summary dictionary."""
    return {
        "word_count": word_count(text),
        "reversed": reverse_text(text),
        "is_palindrome": is_palindrome(text),
    }