"""
Write an algorithm to find the "next" node (in-order successor) of a given
node in a BST. You may assume that each node has a link to its parent.
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

def find_successor(node: Node) -> Node or None:
    if node is None:
        return None

    if node.right:
        return find_min(node.right)
    else:
        p = node.parent

        while p is not None and p.left != node:
            node = p
            p = p.parent
        
        return p

def find_min(node: Node) -> Node:
    if node is None:
        return None

    while node.left is not None:
        node = node.left

    return node
