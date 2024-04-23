class Node:
    def __init__(self, val):
        self.val = val
        self.children = []


def build_tree(s):
    stack = []
    root = None
    for c in s:
        if c == '(':
            stack.append(curr)
        elif c == ')':
            stack.pop()
        elif c != ',':
            curr = Node(c)
            if not root:
                root = curr
            else:
                stack[-1].children.append(curr)
    return root


s = 'A(B(E,F),C(G(J)),D(H,I(K,L,M)))'
root = build_tree(s)


def print_tree(node, level=0):
    if not node:
        return
    print('  ' * level + node.val)
    for child in node.children:
        print_tree(child, level+1)


print_tree(root)
