class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def convert_to_binary_tree(root):
    if not root:
        return None
    stack = [root]
    binary_root = TreeNode(root.val)
    binary_node = binary_root
    while stack:
        node = stack.pop()
        if node.right:
            stack.append(node.right)
            binary_node.right = TreeNode(node.right.val)
            binary_node = binary_node.right
        if node.left:
            stack.append(node.left)
            binary_node.left = TreeNode(node.left.val)
            binary_node = binary_node.left
    return binary_root


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

binary_tree = convert_to_binary_tree(root)
