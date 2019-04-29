from ctci.p4_5 import is_search, Node

def test_is_search():
    tree = Node(1, Node(1))

    assert not is_search(tree)

    tree = Node(2, Node(1), Node(3))

    assert is_search(tree)

    tree = Node(10, Node(5), Node(15, Node(6), Node(20)))

    assert not is_search(tree)
