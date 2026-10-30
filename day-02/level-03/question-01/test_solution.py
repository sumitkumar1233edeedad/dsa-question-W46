import unittest

class TestCheckPairSumExists(unittest.TestCase):
    def test_example1(self):
        self.assertTrue(check_pair_sum_exists([2, 7, 11, 15], 9))

    def test_example2(self):
        self.assertTrue(check_pair_sum_exists([2, 3, 4], 6))

    def test_example3(self):
        self.assertTrue(check_pair_sum_exists([-1, 0], -1))

    def test_example4(self):
        self.assertFalse(check_pair_sum_exists([1, 2, 3, 4], 10))

    def test_duplicates(self):
        self.assertTrue(check_pair_sum_exists([1, 2, 2, 3], 4))  # 2+2=4

    def test_negative_numbers(self):
        self.assertTrue(check_pair_sum_exists([-5, -3, 0, 2, 4], -8))  # -5 + -3 = -8

    def test_no_pair(self):
        self.assertFalse(check_pair_sum_exists([1, 2, 3], 7))

    def test_minimal_length(self):
        self.assertTrue(check_pair_sum_exists([5, 5], 10))
        self.assertFalse(check_pair_sum_exists([5, 6], 10))

if __name__ == "__main__":
    unittest.main()
