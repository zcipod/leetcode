import unittest
from red_black_tree import RedBlackTree


class MyTestCase(unittest.TestCase):
    @staticmethod
    def init_tree() -> RedBlackTree:
        """before the testing, init a whole red-black tree:
                               50
                          /        \
                         40          60
                       /   \      /    \
                     20R   45    55R   70R
                    /  \       /   \   /  \
                   10  30     51  56  65  75
                             """
        left = RedBlackTree(10, 'Black')
        right = RedBlackTree(30, 'Black')
        root = RedBlackTree(20, left=left, right=right)
        left.parent = root
        right.parent = root
        left = root
        right = RedBlackTree(45, 'Black')
        root = RedBlackTree(40, 'Black', left=left, right=right)
        left.parent = root
        right.parent = root
        left_reserve = root
        left = RedBlackTree(51, "Black")
        right = RedBlackTree(56, "Black")
        root1 = RedBlackTree(55, left=left, right=right)
        left.parent = root1
        right.parent = root1
        left = RedBlackTree(65, "Black")
        right = RedBlackTree(75, 'Black')
        root2 = RedBlackTree(70, left=left, right= right)
        left.parent = root2
        right.parent = root2
        root3 = RedBlackTree(60, "Black", left=root1, right=root2)
        root1.parent = root3
        root2.parent = root3
        root = RedBlackTree(50, "Black", left=left_reserve, right=root3)
        left_reserve.parent = root
        root3.parent = root
        return root

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

    def test_find(self):
        root = self.init_tree()
        self.assertEqual(root.find(10).val, 10)
        self.assertEqual(root.find(20).color, "Red")
        self.assertEqual(root.find(55).left.val, 51)
        self.assertEqual(root.find(65).parent.val, 70)
        self.assertEqual(root.find(9), None)

    def test_insert(self):
        root = self.init_tree()
        self.assertEqual(root.insert(9).val, 9)
        self.assertEqual(root.left.left.left.left.val, 9)
        self.assertEqual(root.left.left.left.left.color, "Red")
        self.assertEqual(root.left.left.left.size, 2)
        self.assertEqual(root.left.left.left.left.parent.val, 10)
        root.insert(8)
        self.assertEqual(root.left.left.left.val, 9)
        self.assertEqual(root.left.left.left.color, "Black")
        self.assertEqual(root.left.left.left.left.val, 8)
        self.assertEqual(root.left.left.left.right.color, "Red")
        self.assertEqual(root.left.left.left.left.color, "Red")
        with self.assertRaises(ValueError):
            root.insert(10)


    def test_delete_left(self):
        pass

    def test_delete_right(self):
        pass

    def test_add_left(self):
        pass

    def test_add_right(self):
        pass


if __name__ == '__main__':
    unittest.main()
