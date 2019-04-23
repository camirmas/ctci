from ctci.p2_1 import Node, remove_dups

def test_remove_dups():
    l = Node(1, Node(2, Node(3, Node(1))))

    assert l.length() == 4

    remove_dups(l)

    assert l.length() == 3

    assert l.to_list() == [1, 2, 3]
