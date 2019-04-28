"""
Given a binary tree, design an algorithm which creates a linked list of all
the nodes at each depth.
"""

class LinkedListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def find_depths(node: TreeNode) -> list:
    depths = {}
    depths[0] = LinkedListNode(node.value)
    queue = [(0, node)]

    while len(queue) > 0:
        depth, n = queue[0]
        queue = queue[1:]
        
        if depth not in depths:
            depths[depth] = LinkedListNode(n.value)
        else:
            current = depths[depth]
            new = LinkedListNode(n.value, current)
            depths[depth] = new
        
        depth += 1
        if n.left is not None:
            queue.append((depth, n.left))

        if n.right is not None:
            queue.append((depth, n.right))

    return list(depths.values())
