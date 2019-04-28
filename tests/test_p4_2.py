from ctci.p4_2 import build_tree

def test_build_tree():
    l = [1, 2, 3, 4, 5]

    node = build_tree(l)

    res = []
    in_order(node, res)
    assert res == l

    l = [1, 2, 3, 4]

    node = build_tree(l)

    res = []
    in_order(node, res)
    assert res == l

def in_order(node, vals):
    if node == None:
        return vals

    in_order(node.left, vals)
    vals.append(node.value)
    in_order(node.right, vals)
