import unittest
from RedBlackTree import RedBlackTree


class MyTestCase(unittest.TestCase):
    def test_init(self):
        left = RedBlackTree(5, 'Black')
        right = RedBlackTree(9, 'Black')
        root = RedBlackTree(8, 'Black', left, right)
        self.assertEqual([left.is_black(),
                          right.is_black(),
                          root.is_black(),
                         root.left.val,
                         root.right.val,
                          right.val,
                          left.val],
                         [True, True, True, left.val, right.val, 9, 5])
        left = RedBlackTree(5, parent=root)
        right = RedBlackTree(9, 'Black', parent=root)
        self.assertEqual([left.parent.val, right.parent.val, left.color], [8, 8, 'Red'])
        self.assertEqual([left.size, right.size, root.size], [1, 1, 3])

    def test_isblack(self):
        node = RedBlackTree(5)
        self.assertEqual(node.is_black(), node.color == 'Black')

    def test_set_black(self):
        node = RedBlackTree(5)
        node.set_black()
        self.assertEqual(node.is_black(), True)
        self.assertEqual(node.color, 'Black')
        node = RedBlackTree(5, 'Black')
        node.set_black()
        self.assertEqual(node.is_black(), True)
        self.assertEqual(node.color, 'Black')

    def test_set_red(self):
        node = RedBlackTree(5)
        node.set_red()
        self.assertEqual(node.is_black(), False)
        self.assertEqual(node.color, 'Red')
        node = RedBlackTree(5, 'Black')
        node.set_red()
        self.assertEqual(node.is_black(), False)
        self.assertEqual(node.color, 'Red')

    def test_left_rotate(self):
        child = RedBlackTree(8, 'Red')
        n = RedBlackTree(4, 'Red', right=child)
        parent = RedBlackTree(2, 'Black', right=n)
        child.parent = n
        n.parent = parent
        n.left_rotate()
        self.assertEqual(n.left.val, parent.val)
        self.assertEqual(n.right.val, child.val)
        self.assertEqual(parent.parent.val, n.val)
        self.assertEqual(child.parent.val, n.val)

    def test_right_rotate(self):
        child = RedBlackTree(2, 'Red')
        n = RedBlackTree(4, 'Red', left=child)
        parent = RedBlackTree(8, 'Black', left=n)
        child.parent = n
        n.parent = parent
        n.right_rotate()
        self.assertEqual(n.right.val, parent.val)
        self.assertEqual(n.left.val, child.val)
        self.assertEqual(parent.parent.val, n.val)
        self.assertEqual(child.parent.val, n.val)


if __name__ == '__main__':
    unittest.main()
