# We write the integers of A and B (in the order they are given) on two separate
#  horizontal lines. 
# 
#  Now, we may draw connecting lines: a straight line connecting two numbers A[i
# ] and B[j] such that: 
# 
#  
#  A[i] == B[j]; 
#  The line we draw does not intersect any other connecting (non-horizontal) lin
# e. 
#  
# 
#  Note that a connecting lines cannot intersect even at the endpoints: each num
# ber can only belong to one connecting line. 
# 
#  Return the maximum number of connecting lines we can draw in this way. 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: A = [1,4,2], B = [1,2,4]
# Output: 2
# Explanation: We can draw 2 uncrossed lines as in the diagram.
# We cannot draw 3 uncrossed lines, because the line from A[1]=4 to B[2]=4 will 
# intersect the line from A[2]=2 to B[1]=2.
#  
# 
#  
#  Example 2: 
# 
#  
# Input: A = [2,5,1,2,5], B = [10,5,2,1,5,2]
# Output: 3
#  
# 
#  
#  Example 3: 
# 
#  
# Input: A = [1,3,7,1,7,5], B = [1,9,2,5,1]
# Output: 2 
# 
#  
#  
#  
# 
#  Note: 
# 
#  
#  1 <= A.length <= 500 
#  1 <= B.length <= 500 
#  1 <= A[i], B[i] <= 2000 
#  
#  Related Topics Array

from typing import List
import decorator_time
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        '''posision_A = {}
        for i in range(len(A)):
            if A[i] not in posision_A:
                posision_A[A[i]] = [i]
            else:
                posision_A[A[i]].append(i)
        posision_B = []
        for i in B:
            if i in posision_A:
                posision_B.append(posision_A[i])

        print(posision_A, posision_B)'''
        DP = [[0] * len(B) for _ in range(len(A))]
        DP[0][0] = 1 if A[0] == B[0] else 0
        for j in range(1, len(B)):
            DP[0][j] = 1 if A[0] == B[j] or DP[0][j - 1] else 0
        for i in range(1, len(A)):
            DP[i][0] = 1 if A[i] == B[0] or DP[i - 1][0] else 0
        for i in range(1, len(A)):
            for j in range(1, len(B)):
                DP[i][j] = DP[i - 1][j] + 1 if A[i] == B[j] and DP[i - 1][j - 1] == DP[i - 1][j] else max(DP[i - 1][j], DP[i][j - 1])
        return DP[-1][-1]
# leetcode submit region end(Prohibit modification and deletion)


@decorator_time.count_time
def main():
    sopj = Solution()
    print(sopj.maxUncrossedLines(A = [1,3,7,1,7,5], B = [1,9,2,5,1]))

main()