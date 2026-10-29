import unittest

class TestTwoSumSorted(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(two_sum_sorted([2, 7, 11, 15], 9), [1, 2])
    
    def test_example2(self):
        self.assertEqual(two_sum_sorted([2, 3, 4], 6), [1, 3])
    
    def test_example3(self):
        self.assertEqual(two_sum_sorted([-1, 0], -1), [1, 2])
    
    def test_negative_numbers_unique(self):
        # Only -5 + 0 = -5
        self.assertEqual(two_sum_sorted([-5, -3, 0, 2, 4, 6], -5), [1, 3])
    
    def test_large_array_unique(self):
        # Only 1 + 2 = 3
        numbers = list(range(1, 30001))
        self.assertEqual(two_sum_sorted(numbers, 3), [1, 2])
    
    def test_duplicates_unique(self):
        # Only 1 + 1 = 2 (two 1's at indices 1 and 2)
        self.assertEqual(two_sum_sorted([1, 1, 2, 2], 2), [1, 2])
    
    def test_two_elements(self):
        self.assertEqual(two_sum_sorted([1, 2], 3), [1, 2])

if __name__ == '__main__':
    unittest.main()
