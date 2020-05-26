import unittest
from UncrossedLines import Solution


class MyTestCase(unittest.TestCase):
    def test_maxUncrossedLines(self):
        s = Solution()
        self.assertEqual(s.maxUncrossedLines(A=[2, 5, 1, 2, 5], B=[10, 5, 2, 1, 5, 2]), 3)
        self.assertEqual(s.maxUncrossedLines(A=[1, 3, 7, 1, 7, 5], B=[1, 9, 2, 5, 1]), 2)

if __name__ == '__main__':
    unittest.main()
