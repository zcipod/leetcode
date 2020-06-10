import unittest
from CountNumberOfTeams import Solution

class MyTestCase(unittest.TestCase):
    def test_numTeams(self):
        s = Solution()
        self.assertEqual(s.numTeams([2, 5, 3, 4, 1]), 3)
        self.assertEqual(s.numTeams([2, 1, 3]), 0)
        self.assertEqual(s.numTeams([1,2,3,4]), 4)
        self.assertEqual(s.numTeams([2,5,3,7,8,9,43,23,47,91,12,34,61,28,4,1]), 265)


if __name__ == '__main__':
    unittest.main()
