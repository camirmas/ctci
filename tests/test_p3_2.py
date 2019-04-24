from ctci.p3_2 import Stack

def test_stack_min():
    s = Stack()

    assert s.min() is None

    s.push(8)

    assert s.min() == 8

    s.push(1)

    assert s.min() == 1

    s.pop()

    assert s.min() == 8
