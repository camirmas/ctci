from ctci.p3_1 import StackManager

def test_stack_manager_init():
    s = StackManager()

    assert s.stacks == []
    assert s.top == {
        1: None,
        2: None,
        3: None,
    }

def test_stack_manager_push():
    s = StackManager()

    s.push(1, 1)

    assert s.top == {
        1: 0,
        2: None,
        3: None,
    }

    s.push(2, 2)
    assert s.top == {
        1: 0,
        2: 1,
        3: None,
    }

    s.push(3, 3)

    assert s.stacks == [1, 2, 3]
    assert s.top == {
        1: 0,
        2: 1,
        3: 2,
    }

    s.push(1, 4)

    assert s.stacks == [1, 4, 2, 3]
    assert s.top == {
        1: 1,
        2: 2,
        3: 3,
    }

def test_stack_manager_pop():
    s = StackManager()

    assert s.pop(1) is None

    s.push(1, 1)

    assert s.pop(1) == 1
    assert s.length[1] == 0
    assert s.top[1] == None

    s.push(1, 1)
    s.push(2, 2)
    s.push(3, 3)

    assert s.pop(2) == 2
    assert s.length[2] == 0
    assert s.top == {
        1: 0,
        2: None,
        3: 1,
    }
