class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branch_sums(root):
    def left_search(node, is_left, suma):
        if node is None:
            return 0

        if node.left is None and node.right is None and is_left:
            return node.value

        left_sum = left_search(node.left, True, suma)
        right_sum = left_search(node.right, False, suma)

        return left_sum + right_sum

    return left_search(root, False, 0)


"""
if __name__ == '__main__':
    root = BinaryTree(3)
    root.left = BinaryTree(9)
    root.left.left = BinaryTree(8)
    root.right = BinaryTree(20)
    root.right.left = BinaryTree(15)
    root.right.right = BinaryTree(7)
    root.right.right.left = BinaryTree(5)
    print(branch_sums(root))"""
