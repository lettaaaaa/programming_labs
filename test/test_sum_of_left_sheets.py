import unittest
from src.sum_of_left_sheets import BinaryTree, branch_sums


class TestBranchSums(unittest.TestCase):
    def setUp(self):
        self.root = BinaryTree(3)
        self.root.left = BinaryTree(9)
        self.root.left.left = BinaryTree(8)
        self.root.right = BinaryTree(20)
        self.root.right.left = BinaryTree(15)
        self.root.right.right = BinaryTree(7)
        self.root.right.right.left = BinaryTree(5)

    def test_branch_sums(self):
        self.assertEqual(branch_sums(self.root), 28)

    def test_empty_tree(self):
        empty_root = None
        self.assertEqual(branch_sums(empty_root), 0)


if __name__ == '__main__':
    unittest.main()
