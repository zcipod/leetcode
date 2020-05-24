# Given two lists of closed intervals, each list of intervals is pairwise disjoi
# nt and in sorted order. 
# 
#  Return the intersection of these two interval lists. 
# 
#  (Formally, a closed interval [a, b] (with a <= b) denotes the set of real num
# bers x with a <= x <= b. The intersection of two closed intervals is a set of re
# al numbers that is either empty, or can be represented as a closed interval. For
#  example, the intersection of [1, 3] and [2, 4] is [2, 3].) 
# 
#  
#  
# 
#  Example 1: 
# 
#  
# 
#  
# Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
# Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
# Reminder: The inputs and the desired output are lists of Interval objects, and
#  not arrays or lists.
#  
# 
#  
# 
#  Note: 
# 
#  
#  0 <= A.length < 1000 
#  0 <= B.length < 1000 
#  0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9 
#  
# 
#  NOTE: input types have been changed on April 15, 2019. Please reset to defaul
# t code definition to get new method signature. 
#  
#  Related Topics Two Pointers
from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        def find_cross(a: List[int], b: List[int]) -> (List[int], int):
            if max(a[0], b[0]) > min(a[1], b[1]):
                return ([], 1) if a[1] < b[1] else ([], 2)  # 返回右边界小的list
            return ([max(a[0], b[0]), min(a[1], b[1])], 1) if a[1] < b[1] else ([max(a[0], b[0]), min(a[1], b[1])], 2)

        point_a = 0
        point_b = 0
        res = []
        while point_a < len(A) and point_b < len(B):
            temp = find_cross(A[point_a], B[point_b])
            if len(temp[0]):
                res.append(temp[0])
            if temp[1] == 1:
                point_a += 1
            else:
                point_b += 1
        return res
# leetcode submit region end(Prohibit modification and deletion)


def main():
    sopj = Solution()
    print(sopj.intervalIntersection(A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]))

main()