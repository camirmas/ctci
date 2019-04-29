from ctci.p4_4 import is_balanced, Node

def test_is_balanced():
    tree = Node(0)

    assert is_balanced(tree)

    tree = Node(0, Node(1), Node(2, Node(3), Node(4)))

    assert is_balanced(tree)

    tree = Node(0, Node(1), Node(2, Node(3), Node(4, Node(5))))
    
    assert not is_balanced(tree)

    tree = Node(0, Node(1, Node(2)))

    assert not is_balanced(tree)
