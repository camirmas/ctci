from ctci.p1_8 import zero_matrix

def test_zero_matrix():
    l = [
        [0, 1, 2],
        [1, 1, 1],
        [1, 1, 1],
    ]

    zero_matrix(l)

    assert l == [
        [0, 0, 0],
        [0, 1, 1],
        [0, 1, 1],
    ]

    l = [
        [1, 0, 2],
        [1, 1, 1],
        [1, 1, 1],
    ]

    zero_matrix(l)

    assert l == [
        [0, 0, 0],
        [1, 0, 1],
        [1, 0, 1],
    ]
