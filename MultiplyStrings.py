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
    def multiply(self, num1: str, num2: str) -> str:
        """plus in the target list, avoid too much operation of list and string"""
        if num1 == '0' or num2 == '0':
            return '0'
        res = [0] * (len(num1) + len(num2))
        num1 = list(num1)[::-1]
        num2 = list(num2)[::-1]
        for i in range(len(num1)):
            for j in range(len(num2)):
                product = int(num1[i]) * int(num2[j]) + res[i + j]
                res[i + j] = product % 10
                res[i + j + 1] += product // 10
        if res[-1] >= 10:
            res[-1] %= 10
            res.append(res[-1] // 10)
        res = [str(i) for i in res[::-1]]
        return "".join(res).lstrip('0')

# leetcode submit region end(Prohibit modification and deletion)


@decorator_time.count_time
def main():
    sopj = Solution()
    print(sopj.multiply("2925", "4787"))

main()