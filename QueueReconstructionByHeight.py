# Suppose you have a random list of people standing in a queue. Each person is d
# escribed by a pair of integers (h, k), where h is the height of the person and k
#  is the number of people in front of this person who have a height greater than 
# or equal to h. Write an algorithm to reconstruct the queue. 
# 
#  Note: 
# The number of people is less than 1,100. 
#  
# 
#  Example 
# 
#  
# Input:
# [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
# 
# Output:
# [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
#  
# 
#  
#  Related Topics Greedy

from typing import List
import decorator_time
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        peoplesort = sorted(people)
        res = [0] * len(people)
        for i in range(len(people)):
            count = 0
            for j in range(len(people)):
                if res[j] == 0 and count == peoplesort[i][1]:
                    break
                if res[j] == 0 or res[j][0] == peoplesort[i][0]:
                    count += 1
            res[j] = peoplesort[i]
        return res
        
# leetcode submit region end(Prohibit modification and deletion)


@decorator_time.count_time
def main():
    sopj = Solution()
    print(sopj.reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))

main()