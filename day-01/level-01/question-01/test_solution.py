import unittest

class TestReverseString(unittest.TestCase):
    def test_example1(self):
        s = ["h", "e", "l", "l", "o"]
        reverseString(s)
        self.assertEqual(s, ["o", "l", "l", "e", "h"])

    def test_example2(self):
        s = ["H", "a", "n", "n", "a", "h"]
        reverseString(s)
        self.assertEqual(s, ["h", "a", "n", "n", "a", "H"])

    def test_example3(self):
        s = ["a"]
        reverseString(s)
        self.assertEqual(s, ["a"])

    def test_even_length(self):
        s = ["a", "b", "c", "d"]
        reverseString(s)
        self.assertEqual(s, ["d", "c", "b", "a"])

    def test_odd_length(self):
        s = ["1", "2", "3", "4", "5"]
        reverseString(s)
        self.assertEqual(s, ["5", "4", "3", "2", "1"])

    def test_all_same_characters(self):
        s = ["x", "x", "x", "x"]
        reverseString(s)
        self.assertEqual(s, ["x", "x", "x", "x"])

    def test_in_place_modification(self):
        s = ["a", "b", "c"]
        original_id = id(s)
        reverseString(s)
        self.assertEqual(id(s), original_id)  # Ensure same list object
        self.assertEqual(s, ["c", "b", "a"])

if __name__ == "__main__":
    unittest.main()
