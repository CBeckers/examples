class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
    
if __name__ == "__main__":
    # tree looks like this:
    #
    #      4
    #    /   \
    #   2     6
    #  / \   / \
    # 1   3 5   7

    # layer 3
    root = TreeNode(4)

    # layer 2
    root.left = TreeNode(2)
    root.right = TreeNode(6)

    # layer 1
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)

    root.right.left = TreeNode(5)
    root.right.right = TreeNode(7)


    # how to get values
    print(root.val)
    print(root.left.val)
    print(root.left.left.val)
    print(root.left.right.val)
    print(root.right.val)
    print(root.right.left.val)
    print(root.right.right.val)