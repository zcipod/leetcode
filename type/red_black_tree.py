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
    value, color, left node, right node, parent node"""
    val = None
    color = ""
    left = None
    right = None
    parent = None

    def __init__(self, val, color="Red", left=None, right=None, parent=None):
        self.val = val
        self.color = color
        self.left = left
        self.right = right
        self.parent = parent

    def __str__(self):
        return "".join([self.color, "_Node: ", str(self.val)])

    def __repr__(self):
        return self.__str__()

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
        par.right = None
        self.left = par
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
        par.left = None
        self.right = par
        par.color = 'Red'
        self.color = 'Black'

    def find(self, num):
        """find a specific num in the time of O(logn)
        if the num is not exist in the tree, return None
        or return the tree node whose val equals the num"""
        if self.val == num:
            return self
        if num < self.val:
            return self.left.find(num) if self.left is not None else None
        if num > self.val:
            return self.right.find(num) if self.right is not None else None

    def insert(self, num):
        """insert a num(node) to a tree"""
        if self.val == num:
            raise ValueError('the num is already EXIST!')
        if num < self.val:
            if self.left is not None:
                res = self.left.insert(num)
                return res
            else:
                res = RedBlackTree(num, parent=self)
                self.left = res
                if self.color == "Red":
                    if self.val == self.parent.left.val:
                        self.right_rotate()
                    else:
                        parent = self.parent
                        self.left = None
                        self.parent = res
                        res.right = self
                        res.parent = parent
                        parent.right = res
                        res.left_rotate()
                return res
        elif num > self.val:
            if self.right is not None:
                res = self.right.insert(num)
                return res
            else:
                res = RedBlackTree(num, parent=self)
                self.right = res
                if self.color == "Red":
                    if self.val == self.parent.right.val:
                        self.left_rotate()
                    else:
                        parent = self.parent
                        self.right = None
                        self.parent = res
                        res.left = self
                        res.parent = parent
                        parent.left = res
                        res.right_rotate()
                return res
