from ctci.p1_7 import rotate

def test_rotate():
    l = [
        [0, 1],
        [2, 3],
    ]

    rotate(l)
    
    assert l == [
        [2, 0],
        [3, 1],
    ]

    l = [
        [0, 0, 0, 0],
        [1, 1, 1, 1],
        [2, 2, 2, 2],
        [3, 3, 3, 3],
    ]

    rotate(l)

    assert l == [
        [3, 2, 1, 0],
        [3, 2, 1, 0],
        [3, 2, 1, 0],
        [3, 2, 1, 0],
    ]