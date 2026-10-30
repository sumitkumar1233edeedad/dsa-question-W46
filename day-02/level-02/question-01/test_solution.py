import unittest

class TestRemoveElement(unittest.TestCase):
    def test_example1(self):
        nums = [3, 2, 2, 3]
        val = 3
        expected_k = 2
        expected_elements = [2, 2]
        k = remove_element(nums, val)
        self.assertEqual(k, expected_k)
        self.assertEqual(sorted(nums[:k]), sorted(expected_elements))
    
    def test_example2(self):
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        val = 2
        expected_k = 5
        expected_elements = [0, 1, 3, 0, 4]
        k = remove_element(nums, val)
        self.assertEqual(k, expected_k)
        self.assertEqual(sorted(nums[:k]), sorted(expected_elements))
    
    def test_empty_list(self):
        nums = []
        val = 5
        expected_k = 0
        k = remove_element(nums, val)
        self.assertEqual(k, expected_k)
        self.assertEqual(nums[:k], [])
    
    def test_single_element_not_equal(self):
        nums = [1]
        val = 2
        expected_k = 1
        expected_elements = [1]
        k = remove_element(nums, val)
        self.assertEqual(k, expected_k)
        self.assertEqual(nums[:k], expected_elements)
    
    def test_single_element_equal(self):
        nums = [2]
        val = 2
        expected_k = 0
        k = remove_element(nums, val)
        self.assertEqual(k, expected_k)
        self.assertEqual(nums[:k], [])
    
    def test_all_elements_equal(self):
        nums = [3, 3, 3]
        val = 3
        expected_k = 0
        k = remove_element(nums, val)
        self.assertEqual(k, expected_k)
        self.assertEqual(nums[:k], [])
    
    def test_no_elements_equal(self):
        nums = [1, 2, 3]
        val = 4
        expected_k = 3
        expected_elements = [1, 2, 3]
        k = remove_element(nums, val)
        self.assertEqual(k, expected_k)
        self.assertEqual(sorted(nums[:k]), sorted(expected_elements))

if __name__ == "__main__":
    unittest.main()