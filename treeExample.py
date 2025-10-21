class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def print_tree(node):
    if node is None:
        return
    print(node.val)

    # go to the next nodes recursively
    print_tree(node.left)
    print_tree(node.right)

def set_tree():
    # layer 0
    root = TreeNode(4)

    # layer 1
    root.left = TreeNode(2)
    root.right = TreeNode(6)

    # layer 2
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(7)

    return root


if __name__ == "__main__":
    # tree looks like this:
    #
    #      4       layer 0
    #    /   \
    #   2     6    layer 1
    #  / \   / \
    # 1   3 5   7  layer 2

    root = set_tree()
    print_tree(root)