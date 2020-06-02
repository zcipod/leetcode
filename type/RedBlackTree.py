#!/usr/bin/env python
#coding:utf-8
"""
build red black tree: root = TreeNode(val, left, right)
note: left & right must be TreeNode

build complex tree from array: root = TreeNode.createTree(array)

draw the whole tree: root.draw_tree()
this method is avaliable for any TreeNode
"""
__version__=            "1.0.0"
__author__=             "Kevin"
__date__=               "Tue Jun 02 10:00:00 2020"
__copyright__=          ""


from typing import List


class RedBlackTree:
    """Red Black Tree type, includes attributes:
    value, color, left node, right node, parent node and the size of the tree
    the attribute of size is not good right now,
    it can only calculate while defining, it is the sum of node numbers of its
    children, including itself"""
    val = None
    color = ""
    left = None
    right = None
    parent = None
    size = 1

    def __init__(self, val, color="Red", left=None, right=None, parent=None):
        self.val = val
        self.color = color
        self.left = left
        self.right = right
        self.parent = parent
        self.size = 1
        if left is not None:
            self.size += left.size
        if right is not None:
            self.size += right.size

    def is_black(self):
        """check if the node is black node or not"""
        return self.color == "Black"

    def set_black(self):
        """set the node to a black node, no matter it was black or red"""
        self.color = "Black"

    def set_red(self):
        """set the node to a red node, no matter it was black or red"""
        self.color = "Red"

    def print_out(self) -> List[int]:
        """reveal all the values of this tree and its children
        in this method, medium traversal is used"""
        res = []
        if self.left:
            res += self.left.print_out()
        res.append(self.val)
        if self.right:
            res += self.right.print_out()
        return res

    def left_rotate(self):
        """conduct left rotation on a red node
        this method is used when two continues red nodes occurs
        it is used by the centre node
        it will become the parent node and a black node after rotation"""
        par = self.parent
        gra_par = par.parent
        if gra_par is not None and par.val > gra_par.val:
            gra_par.right = self
            self.parent = gra_par
        elif gra_par is not None:
            gra_par.left = self
            self.parent = gra_par
        par.parent = self
        par.size -= par.right.size
        par.right = None
        self.left = par
        self.size += par.size
        par.color = 'Red'
        self.color = 'Black'

    def right_rotate(self):
        """conduct right rotation on a red node
                this method is used when two continues red nodes occurs
                it is used by the centre node
                it will become the parent node and a black node after rotation"""
        par = self.parent
        gra_par = par.parent
        if gra_par is not None and par.val > gra_par.val:
            gra_par.right = self
            self.parent = gra_par
        elif gra_par is not None:
            gra_par.left = self
            self.parent = gra_par
        par.parent = self
        par.size -= par.left.size
        par.left = None
        self.right = par
        self.size += par.size
        par.color = 'Red'
        self.color = 'Black'


c = RedBlackTree(8, 'Red')
n = RedBlackTree(4, 'Red', right=c)
a = RedBlackTree(2, 'Black',right=n)
c.parent = n
n.parent = a
n.left_rotate()

print(n.print_out())
