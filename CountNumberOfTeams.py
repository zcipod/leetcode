# There are n soldiers standing in a line. Each soldier is assigned a unique rat
# ing value. 
# 
#  You have to form a team of 3 soldiers amongst them under the following rules:
#  
# 
#  
#  Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rat
# ing[k]). 
#  A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > ratin
# g[j] > rating[k]) where (0 <= i < j < k < n). 
#  
# 
#  Return the number of teams you can form given the conditions. (soldiers can b
# e part of multiple teams). 
# 
#  
#  Example 1: 
# 
#  
# Input: rating = [2,5,3,4,1]
# Output: 3
# Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (
# 5,3,1). 
#  
# 
#  Example 2: 
# 
#  
# Input: rating = [2,1,3]
# Output: 0
# Explanation: We can't form any team given the conditions.
#  
# 
#  Example 3: 
# 
#  
# Input: rating = [1,2,3,4]
# Output: 4
#  
# 
#  
#  Constraints: 
# 
#  
#  n == rating.length 
#  1 <= n <= 200 
#  1 <= rating[i] <= 10^5 
#  Related Topics Array

from typing import List
import decorator_time
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        res = [[0] * 4 for _ in range(len(rating))]
        for i in range(len(rating)):
            res[i][0] = len([x for x in rating[:i] if x < rating[i]])
            res[i][1] = len([x for x in rating[:i] if x > rating[i]])
            if res[i][0]:
                res[i][2] = len([x for x in rating[i:] if x > rating[i]])
            if res[i][1]:
                res[i][3] = len([x for x in rating[i:] if x < rating[i]])
        return sum([x[0] * x[2] + x[1] * x[3] for x in res])

# leetcode submit region end(Prohibit modification and deletion)


@decorator_time.count_time
def main():
    sopj = Solution()
    print(sopj.numTeams([1,2,3,4]))

main()