import unittest

class TestTrapRainWater(unittest.TestCase):
    def test_example1(self):
        height = [0,1,0,2,1,0,1,3,2,1,2,1]
        self.assertEqual(trap(height), 6)

    def test_example2(self):
        height = [4,2,0,3,2,5]
        self.assertEqual(trap(height), 9)

    def test_example3(self):
        height = [5,4,3,2,1]
        self.assertEqual(trap(height), 0)

    def test_empty(self):
        self.assertEqual(trap([]), 0)

    def test_single_element(self):
        self.assertEqual(trap([5]), 0)

    def test_all_same(self):
        self.assertEqual(trap([3,3,3]), 0)

    def test_valley(self):
        height = [3,1,2]
        self.assertEqual(trap(height), 1)

if __name__ == '__main__':
    unittest.main()