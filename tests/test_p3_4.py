from ctci.p3_4 import MyQueue

def test_my_queue():
    q = MyQueue()

    q.add(1)
    q.add(2)
    q.add(3)

    assert q.remove() == 1
    assert q.remove() == 2

    q.add(4)

    assert q.remove() == 3
    assert q.remove() == 4
    assert q.remove() is None
