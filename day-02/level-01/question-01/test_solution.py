import unittest
from typing import List

# Include the solution function so the test is self-contained
def reverse_array(nums: List[int]) -> None:
    """
    Reverses the list nums in-place using the two-pointer technique.
    Modifies the input list directly without allocating extra space.
    """
    left, right = 0, len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

class TestReverseArray(unittest.TestCase):
    def test_standard_odd_length(self):
        nums = [1, 2, 3, 4, 5]
        expected = [5, 4, 3, 2, 1]
        reverse_array(nums)
        self.assertEqual(nums, expected)

    def test_standard_even_length(self):
        nums = [10, -2, 3, 7]
        expected = [7, 3, -2, 10]
        reverse_array(nums)
        self.assertEqual(nums, expected)

    def test_single_element(self):
        nums = [42]
        expected = [42]
        reverse_array(nums)
        self.assertEqual(nums, expected)

    def test_two_elements(self):
        nums = [5, 9]
        expected = [9, 5]
        reverse_array(nums)
        self.assertEqual(nums, expected)

    def test_all_same_elements(self):
        nums = [7, 7, 7, 7]
        expected = [7, 7, 7, 7]
        reverse_array(nums)
        self.assertEqual(nums, expected)

    def test_negative_numbers(self):
        nums = [-1, -5, -3, -2]
        expected = [-2, -3, -5, -1]
        reverse_array(nums)
        self.assertEqual(nums, expected)

if __name__ == '__main__':
    unittest.main()
