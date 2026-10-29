import unittest

class TestValidPalindrome(unittest.TestCase):
    def test_example1(self):
        self.assertTrue(valid_palindrome("aba"))

    def test_example2(self):
        self.assertTrue(valid_palindrome("abca"))

    def test_example3(self):
        self.assertFalse(valid_palindrome("abc"))

    def test_single_char(self):
        self.assertTrue(valid_palindrome("a"))

    def test_two_chars_palindrome(self):
        self.assertTrue(valid_palindrome("aa"))

    def test_two_chars_non_palindrome(self):
        self.assertTrue(valid_palindrome("ab"))

    def test_deeee(self):
        self.assertTrue(valid_palindrome("deeee"))

    def test_cbbcc(self):
        self.assertTrue(valid_palindrome("cbbcc"))

    def test_abcda(self):
        self.assertFalse(valid_palindrome("abcda"))

    def test_long_palindrome(self):
        self.assertTrue(valid_palindrome("racecar"))

    def test_long_non_palindrome(self):
        # "racecarss" cannot become a palindrome with at most one deletion
        self.assertFalse(valid_palindrome("racecarss"))

if __name__ == "__main__":
    unittest.main()