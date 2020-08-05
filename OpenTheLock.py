# 
# You have a lock in front of you with 4 circular wheels. Each wheel has 10 slot
# s: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freel
# y and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each
#  move consists of turning one wheel one slot.
#  
# The lock initially starts at '0000', a string representing the state of the 4 
# wheels.
#  
# You are given a list of deadends dead ends, meaning if the lock displays any o
# f these codes, the wheels of the lock will stop turning and you will be unable t
# o open it.
#  
# Given a target representing the value of the wheels that will unlock the lock,
#  return the minimum total number of turns required to open the lock, or -1 if it
#  is impossible.
#  
# 
#  Example 1: 
#  
# Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
# Output: 6
# Explanation:
# A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "12
# 01" -> "1202" -> "0202".
# Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would
#  be invalid,
# because the wheels of the lock become stuck after the display becomes the dead
#  end "0102".
#  
#  
# 
#  Example 2: 
#  
# Input: deadends = ["8888"], target = "0009"
# Output: 1
# Explanation:
# We can turn the last wheel in reverse to move from "0000" -> "0009".
#  
#  
# 
#  Example 3: 
#  
# Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], t
# arget = "8888"
# Output: -1
# Explanation:
# We can't reach the target without getting stuck.
#  
#  
# 
#  Example 4: 
#  
# Input: deadends = ["0000"], target = "8888"
# Output: -1
#  
#
# 
#  Note: 
#  
#  The length of deadends will be in the range [1, 500]. 
#  target will not be in the list deadends. 
#  Every string in deadends and the string target will be a string of 4 digits f
# rom the 10,000 possibilities '0000' to '9999'. 
#  
#  Related Topics Breadth-first Search 
#  👍 1024 👎 42

from typing import List
import decorator_time

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(deadends)
        if "0000" in visited:return -1
        Q = []
        num = 0
        Q.append("0000")
        while len(Q):
            Q = self.BFS(Q, target, visited)
            if Q is True:
                return num + 1
            else:
                num += 1
        return -1

    def BFS(self,Q, target, visited):
        tempQ = []
        for item in Q:
            for i in range(4):
                changeLetter = (int(item[i]) + 1) % 10
                changeStr = "".join([item[:i], str(changeLetter), item[i+1:]])
                if changeStr == target:return True
                if changeStr not in visited:
                    tempQ.append(changeStr)
                    visited.add(changeStr)
                changeLetter = (int(item[i]) + 9) % 10
                changeStr = "".join([item[:i], str(changeLetter), item[i + 1:]])
                if changeStr not in visited:
                    tempQ.append(changeStr)
                    visited.add(changeStr)
                if changeStr == target: return True
        return tempQ
# leetcode submit region end(Prohibit modification and deletion)


@decorator_time.count_time
def main():
    sopj = Solution()
    print(sopj.openLock(deadends = ["0201","0101","0102","1212","2002"], target = "0202"))

main()