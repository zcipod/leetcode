import unittest
from MultiplyStrings import Solution


class MyTestCase(unittest.TestCase):
    def test_multiply(self):
        s = Solution()
        self.assertEqual(s.multiply(num1="2", num2="3"), "6")
        self.assertEqual(s.multiply(num1="123", num2="456"), "56088")
        self.assertEqual(s.multiply(num1="2925", num2="4787"), "14001975")

    def test_add_string(self):
        s = Solution()
        self.assertEqual(s.add_string(["2","8","6","9","7","8"], ["5","4","3","1","9"]), ["3","4","1","2","9","7"])
        self.assertEqual(s.add_string(["9","9","9","9"], ["9","9","9","9","9"]), ["1","0","9","9","9","8"])
        self.assertEqual(s.add_string(["1"], ["9","9","9","9","9","9"]), ["1","0","0","0","0","0","0"])

    def test_string_add_one(self):
        s = Solution()
        self.assertEqual(s.string_add_one(["3", "4", "1", "2", "9", "7"], ["3", "4", "1", "2", "9", "8"]))
        self.assertEqual(s.string_add_one(["1", "9", "9", "9"], ["2", "0", "0", "0"]))
        self.assertEqual(s.string_add_one(["9", "9", "9", "9"], ["1", "0", "0", "0", "0"]))


if __name__ == '__main__':
    unittest.main()
