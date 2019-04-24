from ctci.queue import Queue

def test_queue_init():
    queue = Queue()

    assert queue.first is None
    assert queue.last is None

def test_queue_add():
    queue = Queue()

    queue.add(1)

    assert queue.first is not None
    assert queue.last is not None
    assert queue.first.data == 1
    assert queue.first is queue.last

    queue.add(2)

    assert queue.first.data == 1
    assert queue.last.data == 2

def test_queue_remove():
    queue = Queue()

    queue.add(1)
    queue.add(2)
    queue.add(3)

    assert queue.remove() == 1
    assert queue.remove() == 2
    assert queue.remove() == 3
    assert queue.remove() == None

def test_queue_peek():
    queue = Queue()

    queue.add(1)
    queue.add(2)
    queue.add(3)

    assert queue.peek() == 1
    assert queue.first.data == 1

def test_queue_is_empty():
    queue = Queue()

    assert queue.is_empty()

    queue.add(1)

    assert not queue.is_empty()
