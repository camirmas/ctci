from ctci.stack import Stack

def test_stack_init():
    s = Stack()

    s.top = None

def test_stack_push():
    s = Stack()
    s.push(1)

    assert s.top.data == 1
    assert s.top.next == None

    s.push(2)
    assert s.top.data == 2
    assert s.top.next.data == 1

def test_stack_pop():
    s = Stack()

    assert s.pop() is None

    s.push(1)

    assert s.pop() == 1
    assert s.pop() is None

    s.push(1)
    s.push(2)
    s.push(3)

    assert s.pop() == 3
    assert s.top.data == 2
    assert s.top.next.data == 1

def test_stack_peek():
    s = Stack()

    assert s.peek() is None

    s.push(1)

    assert s.peek() == 1

def test_stack_is_empty():
    s = Stack()

    assert s.is_empty()

    s.push(1)

    assert not s.is_empty()
