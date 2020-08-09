# Given a binary tree, flatten it to a linked list in-place. 
# 
#  For example, given the following tree: 
# 
#  
#     1
#    / \
#   2   5
#  / \   \
# 3   4   6
#  
# 
#  The flattened tree should look like: 
# 
#  
# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6
#  
#  Related Topics Tree Depth-first Search 
#  👍 2941 👎 339

from typing import List
import decorator_time
from tree_node import TreeNode
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        def get_the_last_node(node) -> TreeNode:
            return node if node.right is None else get_the_last_node(node.right)

        if root is None:
            return
        if root.left:
            self.flatten(root.left)
            temp, root.right, root.left = root.right, root.left, None
            right_tail = get_the_last_node(root)
            right_tail.right = temp
            self.flatten(temp)
        else:
            self.flatten(root.right)
        return
        
# leetcode submit region end(Prohibit modification and deletion)

        
@decorator_time.count_time
def main():
    sopj = Solution()
    null = None
    root = TreeNode.create_tree([1,2,5,3,4,null,6])
    print(sopj.flatten(root))

main()