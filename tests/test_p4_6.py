from ctci.p4_6 import Node, find_successor

def test_find_successor():
    root = Node(2)
    root.left = Node(1)
    root.right = Node(3)
    root.left.parent = root
    root.right.parent = root

    assert find_successor(root).val == 3
    assert find_successor(root.left).val == 2

    root = Node(8)
    root.right = Node(10)
    root.right.parent = root
    root.right.right = Node(11)
    root.right.left = Node(9)
    root.right.right.parent = root.right
    root.right.left.parent = root.right

    assert find_successor(root).val == 9
    assert find_successor(root.right).val == 11
