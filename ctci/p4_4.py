"""
Implement a function to check if a binary tree is balanced. For the purposes
of this question, a balanced tree is defined to be a tree such that the
heights of the two subtrees of any node never differ by more than one.
"""

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def is_balanced(node: Node) -> bool:
    if node is None:
        return True

    left = height(node.left)
    right = height(node.right)

    return (abs(left - right) <= 1
        and is_balanced(node.left) 
        and is_balanced(node.right))

def height(node: Node) -> int:
    if node is None:
        return 0

    left = 1 + height(node.left)
    right = 1 + height(node.right)

    return max(left, right)
