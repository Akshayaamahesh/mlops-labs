import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))
import text_utils


class TestTextUtils(unittest.TestCase):

    def test_word_count(self):
        self.assertEqual(text_utils.word_count("hello world"), 2)

    def test_reverse_text(self):
        self.assertEqual(text_utils.reverse_text("abc"), "cba")

    def test_is_palindrome(self):
        self.assertTrue(text_utils.is_palindrome("racecar"))
        self.assertFalse(text_utils.is_palindrome("hello"))
        self.assertTrue(text_utils.is_palindrome("A man, a plan, a canal: Panama"))

    def test_text_summary(self):
        result = text_utils.text_summary("noon")
        self.assertEqual(result["word_count"], 1)
        self.assertEqual(result["reversed"], "noon")
        self.assertTrue(result["is_palindrome"])

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            text_utils.reverse_text(None)



if __name__ == "__main__":
    unittest.main()