# In a directed graph, we start at some node and every turn, walk along a direct
# ed edge of the graph. If we reach a node that is terminal (that is, it has no ou
# tgoing directed edges), we stop. 
# 
#  Now, say our starting node is eventually safe if and only if we must eventual
# ly walk to a terminal node. More specifically, there exists a natural number K s
# o that for any choice of where to walk, we must have stopped at a terminal node 
# in less than K steps. 
# 
#  Which nodes are eventually safe? Return them as an array in sorted order. 
# 
#  The directed graph has N nodes with labels 0, 1, ..., N-1, where N is the len
# gth of graph. The graph is given in the following form: graph[i] is a list of la
# bels j such that (i, j) is a directed edge of the graph. 
# 
#  
# Example:
# Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
# Output: [2,4,5,6]
# Here is a diagram of the above graph.
# 
#  
# 
#  
# 
#  Note: 
# 
#  
#  graph will have length at most 10000. 
#  The number of edges in the graph will not exceed 32000. 
#  Each graph[i] will be a sorted list of different integers, chosen within the 
# range [0, graph.length - 1]. 
#  
#  Related Topics Depth-first Search Graph 
#  👍 783 👎 145

from typing import List
import decorator_time
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def __init__(self):
        self.isSafe = set()
        self.isNotSafe = set()
        self.visited = set()

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        res = []
        for i in range(len(graph)):
            if len(graph[i]) == 0:
                self.isSafe.add(i)
            if i in self.isSafe:
                res.append(i)
                continue
            self.visited = set()
            if self.dfs(graph, i):
                self.isSafe.add(i)
                res.append(i)
        return res

    def dfs(self, directions, index):
        if len(directions[index]) == 0 or index in self.isSafe:
            return True
        if index in self.isNotSafe or index in self.visited:
            return False
        self.visited.add(index)
        for i in directions[index]:
            if not self.dfs(directions, i):
                self.isNotSafe.add(i)
                return False
        self.isSafe.add(index)
        return True
# leetcode submit region end(Prohibit modification and deletion)


@decorator_time.count_time
def main():
    sopj = Solution()
    print(sopj.eventualSafeNodes([[],[0,2,3,4],[3],[4],[]]))

main()