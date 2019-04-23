from ctci.p1_1 import is_unique

def test_is_unique():
    word = "lightsaber"

    assert is_unique(word)

    word = "palpatine"

    assert not is_unique(word)