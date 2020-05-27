import unittest
from MultiplyStrings import Solution


class MyTestCase(unittest.TestCase):
    def test_multiply(self):
        s = Solution()
        self.assertEqual(s.multiply(num1="2", num2="3"), "6")
        self.assertEqual(s.multiply(num1="123", num2="456"), "56088")
        self.assertEqual(s.multiply(num1="2925", num2="4787"), "14001975")



if __name__ == '__main__':
    unittest.main()
