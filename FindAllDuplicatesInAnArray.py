# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements ap
# pear twice and others appear once. 
# 
#  Find all the elements that appear twice in this array. 
# 
#  Could you do it without extra space and in O(n) runtime? 
#  
#  Example: 
#  
# Input:
# [4,3,2,7,8,2,3,1]
#
# Output:
# [2,3]
#  Related Topics Array 
#  👍 2329 👎 152

from typing import List
import decorator_time
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            if nums[abs(i) - 1] > 0:
                nums[abs(i) - 1] *= -1
            else:
                res.append(abs(i))
        return res
# leetcode submit region end(Prohibit modification and deletion)

        
@decorator_time.count_time
def main():
    sopj = Solution()
    print(sopj.findDuplicates([4,3,2,7,8,2,3,1]))

main()