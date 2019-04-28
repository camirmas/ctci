"""
Given a sorted (increasing order) array with unique integer elements, write an
algorithm to create a binary search tree with minimal height.
"""

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def build_tree(l: list) -> Node or None:
    if len(l) == 0:
        return None

    i = len(l) // 2
    midpoint = l[i]
    left = l[:i]
    right = l[i+1:]

    return Node(midpoint, build_tree(left), build_tree(right))
