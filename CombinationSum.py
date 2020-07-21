# Given a set of candidate numbers (candidates) (without duplicates) and a targe
# t number (target), find all unique combinations in candidates where the candidat
# e numbers sums to target. 
# 
#  The same repeated number may be chosen from candidates unlimited number of ti
# mes. 
# 
#  Note: 
# 
#  
#  All numbers (including target) will be positive integers. 
#  The solution set must not contain duplicate combinations. 
#  
# 
#  Example 1: 
# 
#  
# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
#   [7],
#   [2,2,3]
# ]
#  
# 
#  Example 2: 
# 
#  
# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= candidates.length <= 30 
#  1 <= candidates[i] <= 200 
#  Each element of candidate is unique. 
#  1 <= target <= 500 
#  
#  Related Topics Array Backtracking 
#  👍 3880 👎 118

from typing import List
import decorator_time
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def __init__(self):
        self.res = []

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.find_sub_combination(0, candidates, target) or None

    def find_sub_combination(self, previous_sum, candidates, target):
        min_candidate = min(candidates)
        if previous_sum + min_candidate > target:
            return False
        elif previous_sum + min_candidate == target:
            return [[min_candidate]]
        temp_list = []
        for i in range(len(candidates)):
            if previous_sum + candidates[i] == target:
                temp_list.append([candidates[i]])
            next_level = self.find_sub_combination(previous_sum + candidates[i], candidates[i:], target)
            if next_level:
                for com in next_level:
                    com = [candidates[i]] + com
                    temp_list.append(com)
        return temp_list

# leetcode submit region end(Prohibit modification and deletion)


@decorator_time.count_time
def main():
    sopj = Solution()
    print(sopj.combinationSum([2], 1))

main()