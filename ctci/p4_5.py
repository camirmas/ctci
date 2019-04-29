"""
Implement a function to check if a binary tree is a binary search tree.
"""

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def is_search(node: Node) -> bool:
    sr =[float("-inf"), float("inf")]

    def helper(node, r) -> bool:
        if node is None:
            return True

        if node.value <= r[0] or node.value >= r[1]:
            return False

        left = helper(node.left, [r[0], node.value])
        right = helper(node.right, [node.value, r[1]])

        return left and right

    return helper(node, sr)
