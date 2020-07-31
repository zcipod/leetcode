# There are a total of n courses you have to take, labeled from 0 to n-1. 
# 
#  Some courses may have prerequisites, for example to take course 0 you have to
#  first take course 1, which is expressed as a pair: [0,1] 
# 
#  Given the total number of courses and a list of prerequisite pairs, return th
# e ordering of courses you should take to finish all courses. 
# 
#  There may be multiple correct orders, you just need to return one of them. If
#  it is impossible to finish all courses, return an empty array. 
# 
#  Example 1: 
# 
#  
# Input: 2, [[1,0]] 
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you shou
# ld have finished   
#              course 0. So the correct course order is [0,1] . 
# 
#  Example 2: 
# 
#  
# Input: 4, [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,1,2,3] or [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you shou
# ld have finished both     
#              courses 1 and 2. Both courses 1 and 2 should be taken after you f
# inished course 0. 
#              So one correct course order is [0,1,2,3]. Another correct orderin
# g is [0,2,1,3] . 
# 
#  Note: 
# 
#  
#  The input prerequisites is a graph represented by a list of edges, not adjace
# ncy matrices. Read more about how a graph is represented. 
#  You may assume that there are no duplicate edges in the input prerequisites. 
# 
#  
#  Related Topics Depth-first Search Breadth-first Search Graph Topological Sort
#  
#  👍 2389 👎 133

from typing import List
import decorator_time


# leetcode submit region begin(Prohibit modification and deletion)
import queue
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        degree = [0] * numCourses
        Q = queue.Queue()
        res = []
        for i in prerequisites:
            graph[i[1]].append(i[0])
            degree[i[0]] += 1
        for i in range(numCourses):
            if not degree[i]:
                Q.put(i)
                res.append(i)
        while not Q.empty():
            temp = Q.get()
            for i in graph[temp]:
                degree[i] -= 1
                if not degree[i]:
                    Q.put(i)
                    res.append(i)
        for i in range(numCourses):
            if degree[i]:
                return []
        return res
# leetcode submit region end(Prohibit modification and deletion)


@decorator_time.count_time
def main():
    sopj = Solution()
    print(sopj.findOrder(3, [[1,0],[1,2],[0,1]]))

main()