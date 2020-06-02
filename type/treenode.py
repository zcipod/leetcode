#!/usr/bin/env python
#coding:utf-8
"""
build simple tree: root = TreeNode(val, left, right)
note: left & right must be TreeNode

build complex tree from array: root = TreeNode.createTree(array)

draw the whole tree: root.draw_tree()
this method is available for any TreeNode
"""
__version__=            "1.0.0"
__author__=             "Kevin"
__date__=               "Tue May 12 23:47:49 2020"
__copyright__=          ""


class TreeNode:
    """Tree Node has 4 attributes:
    value, left node, right node and parent node
    the creatTree method is based on medium traversal array"""
    val = None
    left = None
    right = None
    parent = None

    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    def createTree(nums):
        """
        This function is to create a Tree from an array
        Note: every non None element must have two children nodes;
                every None element must not have any children nodes
        :return:
        """
        def buildTree(treeList, nums):
            """
            This fuction is to build the next level nodes
            and link them to the previous level nodes
            """

            if len(nums) == 0:
                return treeList
            nextList = []
            j = 0
            for i in treeList:
                for _ in range(2):
                    if i is not None and j < len(nums):
                        if nums[j] is None:
                            nextList.append(None)
                        else:
                            nextList.append(TreeNode(nums[j]))
                        j += 1
            resList = buildTree(nextList, nums[j:])
            j = 0
            for i in treeList:
                if i is None:
                    continue
                if j < len(resList):
                    if nextList[j] is not None:
                        nextList[j].parent = i
                    i.left = nextList[j]
                    j += 1
                if j < len(resList):
                    if nextList[j] is not None:
                        nextList[j].parent = i
                    i.right = nextList[j]
                    j += 1
            return treeList

        root = TreeNode(nums[0])
        return buildTree([root], nums[1:])[0]

    def draw_tree(self) -> None:
        """
        This function can use turtle to draw a binary tree
        """
        import turtle

        def height(head):
            return 1 + max(height(head.left), height(head.right)) if head else -1

        def jump_to(x, y):
            t.penup()
            t.goto(x, y)
            t.pendown()

        def draw(node, x, y, dx):
            if node:
                t.goto(x, y)
                jump_to(x, y - 20)
                t.write(node.val, align="center", font=("Arial", 15, "normal"))
                t.circle(10)
                draw(node.left, x - dx, y - 50, dx / 2)
                jump_to(x, y - 20)
                draw(node.right, x + dx, y - 50, dx / 2)

        t = turtle.Turtle()
        t.speed(0)
        turtle.delay(0)
        h = height(self)
        jump_to(0, 100 + 10 * h)
        draw(self, 0, 100 + 10 * h, 20 * h)
        t.hideturtle()
        turtle.mainloop()

def main():
    null = None
    nums = [6, 7, 8, 2, 7, null, 3, 9, null, 1, 4, null, null, null, 5]
    root = TreeNode.createTree(nums)
    root.draw_tree()

if __name__ == "__main__":
    main()

