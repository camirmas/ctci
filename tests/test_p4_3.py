from ctci.p4_3 import find_depths, TreeNode

def test_find_depths():
    t = TreeNode(1, TreeNode(2), TreeNode(3))

    res = find_depths(t)

    assert len(res) == 2
    assert res[0].value == 1
    assert res[1].value == 3
    assert res[1].next.value == 2
