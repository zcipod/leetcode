# There are a total of numCourses courses you have to take, labeled from 0 to nu
# mCourses-1. 
# 
#  Some courses may have prerequisites, for example to take course 0 you have to
#  first take course 1, which is expressed as a pair: [0,1] 
# 
#  Given the total number of courses and a list of prerequisite pairs, is it pos
# sible for you to finish all courses? 
# 
#  
#  Example 1: 
# 
#  
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
#              To take course 1 you should have finished course 0. So it is poss
# ible.
#  
# 
#  Example 2: 
# 
#  
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
#              To take course 1 you should have finished course 0, and to take c
# ourse 0 you should
#              also have finished course 1. So it is impossible.
#  
# 
#  
#  Constraints: 
# 
#  
#  The input prerequisites is a graph represented by a list of edges, not adjace
# ncy matrices. Read more about how a graph is represented. 
#  You may assume that there are no duplicate edges in the input prerequisites. 
# 
#  1 <= numCourses <= 10^5 
#  
#  Related Topics Depth-first Search Breadth-first Search Graph Topological Sort
#  
#  👍 3957 👎 180

from typing import List
import decorator_time
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def __init__(self):
        self.record = []
        self.num = 0

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.record = [[set(), set(), False] for _ in range(numCourses)]
        for i in prerequisites:
            self.record[i[0]][0].add(i[1])
            self.record[i[1]][1].add(i[0])
        for i in range(numCourses):
            if self.record[i][2]:
                continue
            if len(self.record[i][0]) == 0:
                self.record[i][2] = True
                self.num += 1
                for target in self.record[i][1]:
                    self.check(target, i)
        return True if self.num == numCourses else False


    def check(self, target, finish):
        self.record[target][0].discard(finish)
        if len(self.record[target][0]) == 0:
            self.record[target][2] = True
            self.num += 1
            for nextTarget in self.record[target][1]:
                self.check(nextTarget, target)
# leetcode submit region end(Prohibit modification and deletion)


@decorator_time.count_time
def main():
    sopj = Solution()
    print(sopj.canFinish(2, [[1,0]]))

main()