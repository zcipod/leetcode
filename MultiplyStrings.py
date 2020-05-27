# Given two non-negative integers num1 and num2 represented as strings, return t
# he product of num1 and num2, also represented as a string. 
# 
#  Example 1: 
# 
#  
# Input: num1 = "2", num2 = "3"
# Output: "6" 
# 
#  Example 2: 
# 
#  
# Input: num1 = "123", num2 = "456"
# Output: "56088"
#  
# 
#  Note: 
# 
#  
#  The length of both num1 and num2 is < 110. 
#  Both num1 and num2 contain only digits 0-9. 
#  Both num1 and num2 do not contain any leading zero, except the number 0 itsel
# f. 
#  You must not use any built-in BigInteger library or convert the inputs to int
# eger directly. 
#  
#  Related Topics Math String

from typing import List
import decorator_time
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def string_add_one(self, pre: List) -> List:
        """let the suffix add one"""
        if len(pre) == 0:
            return ['1']
        if int(pre[-1]) < 9:
            pre[-1] = str(int(pre[-1]) + 1)
            return pre
        else:
            return self.string_add_one(pre[:-1]) + ['0']

    def add_string(self, a: List, b: List) -> List:
        """add two list(num)
        plus all the vertical results"""
        if len(a) < len(b):
            a, b = b, a
        if len(b) == 0:
            return a
        res = ['0'] * (len(a) + 1)
        add_one = 0
        for i in range(1,len(b) + 1):
            temp = int(b[-i]) + int(a[-i]) + add_one
            add_one = 0
            if temp >= 10:
                temp -= 10
                add_one = 1
            res[-i] = str(temp)
        for i in range(len(b) + 1, len(a) + 1):
            temp = int(a[-i]) + add_one
            add_one = 0
            if temp >= 10:
                temp -= 10
                add_one = 1
            res[-i] = str(temp)
        res[0] = str(add_one)
        return res if res[0] != '0' else res[1:]

    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        if len(num1) > len(num2):
            num1, num2 = num2, num1
        matrix = [[int(i) * int(j) for j in num2] for i in num1]
        res = [0] * len(num1)
        for i in range(len(num1)):
            res[i] = list(str(matrix[i][0]))
            for j in range(1, len(num2)):
                if matrix[i][j] >= 10:
                    temp = int(res[i][-1]) + matrix[i][j] // 10
                    if temp >= 10:
                        res[i] = self.string_add_one(res[i][:-1]) + list(str(temp)[-1]) + list(str(matrix[i][j])[-1])
                    else:
                        res[i][-1] = str(temp)
                        res[i].append(str(matrix[i][j] % 10))
                else:
                    res[i].append(str(matrix[i][j]))
        total = []
        for i in range(len(num1)):
            total = self.add_string(total, (res[i] + ['0'] * (len(num1) - 1 - i)))
        return ''.join(total)
# leetcode submit region end(Prohibit modification and deletion)


@decorator_time.count_time
def main():
    sopj = Solution()
    print(sopj.multiply("2925", "4787"))

main()