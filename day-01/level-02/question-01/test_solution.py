import unittest
from typing import List

# The function remove_element is expected to be defined in the same context.
# If running separately, ensure the solution code is imported or defined.

class TestRemoveElement(unittest.TestCase):
    def test_example1(self):
        nums = [3, 2, 2, 3]
        val = 3
        k = remove_element(nums, val)
        self.assertEqual(k, 2)
        self.assertEqual(sorted(nums[:k]), [2, 2])

    def test_example2(self):
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        val = 2
        k = remove_element(nums, val)
        self.assertEqual(k, 5)
        # The first k elements should not contain val
        self.assertTrue(all(x != val for x in nums[:k]))
        # And they should be a permutation of the non-val elements
        expected = [0, 1, 3, 0, 4]
        self.assertEqual(sorted(nums[:k]), sorted(expected))

    def test_empty_array(self):
        nums = []
        val = 5
        k = remove_element(nums, val)
        self.assertEqual(k, 0)
        self.assertEqual(nums, [])

    def test_single_element_not_val(self):
        nums = [1]
        val = 2
        k = remove_element(nums, val)
        self.assertEqual(k, 1)
        self.assertEqual(nums[:k], [1])

    def test_single_element_is_val(self):
        nums = [5]
        val = 5
        k = remove_element(nums, val)
        self.assertEqual(k, 0)
        # nums[:0] is empty

    def test_all_elements_val(self):
        nums = [2, 2, 2, 2]
        val = 2
        k = remove_element(nums, val)
        self.assertEqual(k, 0)

    def test_no_elements_val(self):
        nums = [1, 2, 3, 4]
        val = 5
        k = remove_element(nums, val)
        self.assertEqual(k, 4)
        self.assertEqual(sorted(nums[:k]), [1, 2, 3, 4])

if __name__ == '__main__':
    unittest.main()
