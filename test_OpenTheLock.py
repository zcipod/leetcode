from unittest import TestCase
from OpenTheLock import Solution

class TestSolution(TestCase):
    def test_openLock(self):
        s = Solution()
        self.assertEqual(s.openLock(deadends = ["0201","0101","0102","1212","2002"], target = "0202"), 6)
        self.assertEqual(s.openLock(deadends = ["8888"], target = "0009"), 1)
        self.assertEqual(s.openLock(deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"), -1)
        self.assertEqual(s.openLock(deadends = ["0000"], target = "8888"), -1)
