from ctci.p3_3 import SetOfStacks

def test_set_of_stacks_init():
    s = SetOfStacks(10)

    assert s.capacity == 10
    assert s.current_stack is None

def test_set_of_stacks_push():
    s = SetOfStacks(2)

    s.push(1)

    assert len(s.stacks) == 1

    s.push(2)
    s.push(3)

    assert len(s.stacks) == 2

def test_set_of_stacks_pop():
    s = SetOfStacks(2)

    s.push(1)

    assert len(s.stacks) == 1

    assert s.pop() == 1

    assert len(s.stacks) == 0
    assert s.current_stack is None
    