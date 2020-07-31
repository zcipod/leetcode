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
import queue
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        degree = [0] * numCourses
        Q = queue.Queue()
        for i in prerequisites:
            graph[i[1]].append(i[0])
            degree[i[0]] += 1
        for i in range(numCourses):
            if not degree[i]:
                Q.put(i)
        while not Q.empty():
            temp = Q.get()
            for i in graph[temp]:
                degree[i] -= 1
                if not degree[i]:
                    Q.put(i)
        for i in range(numCourses):
            if degree[i]:
                return False
        return True
# leetcode submit region end(Prohibit modification and deletion)


@decorator_time.count_time
def main():
    sopj = Solution()
    print(sopj.canFinish(7, [[1, 0], [0, 3], [0, 2], [3, 2], [2, 5], [4, 5], [5, 6], [2, 4]]))

main()