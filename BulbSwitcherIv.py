# There is a room with n bulbs, numbered from 0 to n-1, arranged in a row from l
# eft to right. Initially all the bulbs are turned off. 
# 
#  Your task is to obtain the configuration represented by target where target[i
# ] is '1' if the i-th bulb is turned on and is '0' if it is turned off. 
# 
#  You have a switch to flip the state of the bulb, a flip operation is defined 
# as follows: 
# 
#  
#  Choose any bulb (index i) of your current configuration. 
#  Flip each bulb from index i to n-1. 
#  
# 
#  When any bulb is flipped it means that if it is 0 it changes to 1 and if it i
# s 1 it changes to 0. 
# 
#  Return the minimum number of flips required to form target. 
# 
#  
#  Example 1: 
# 
#  
# Input: target = "10111"
# Output: 3
# Explanation: Initial configuration "00000".
# flip from the third bulb:  "00000" -> "00111"
# flip from the first bulb:  "00111" -> "11000"
# flip from the second bulb:  "11000" -> "10111"
# We need at least 3 flip operations to form target. 
# 
#  Example 2: 
# 
#  
# Input: target = "101"
# Output: 3
# Explanation: "000" -> "111" -> "100" -> "101".
#  
# 
#  Example 3: 
# 
#  
# Input: target = "00000"
# Output: 0
#  
# 
#  Example 4: 
# 
#  
# Input: target = "001011101"
# Output: 5
#
#  
#  Constraints: 
# 
#  
#  1 <= target.length <= 10^5 
#  target[i] == '0' or target[i] == '1' 
#  
#  Related Topics String 
#  👍 112 👎 9

from typing import List
import decorator_time
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minFlips(self, target: str) -> int:
        res = 0
        for i in range(len(target)):
            if target[i] == "1":
                res += 1
                break
        for j in range(i + 1, len(target)):
            if target[j] != target[j - 1]:
                res += 1
        return res
# leetcode submit region end(Prohibit modification and deletion)


@decorator_time.count_time
def main():
    sopj = Solution()
    print(sopj.minFlips("000000"))

main()