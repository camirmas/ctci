from ctci.linkedlist import LinkedList

def test_linkedlist():
    l = LinkedList()
    assert l.head == None
    assert l.tail == None

def test_linkedlist_append():
    l = LinkedList()
    l.append(1)

    assert l.find(0) is None
    assert l.find(1) is not None
    assert l.head is not None
    assert l.tail is not None

    l.append(2)
    assert l.head.value == 1
    assert l.tail.value == 2

def test_linkedlist_find():
    l = LinkedList()
    l.append(1)

    node = l.find(1)
    assert node is not None
    assert node.value == 1

def test_linkedlist_find_by():
    l = LinkedList()
    item = {"key": "stuff", "val": 1}
    l.append(item)

    node = l.find_by(lambda item: item["key"] == "stuff")
    assert node is not None
    assert node.value == item

def test_linkedlist_remove():
    l = LinkedList()
    l.append(1)
    l.append(2)
    l.append(3)
    l.append(4)

    # remove at beginning
    assert l.remove(1) == 1
    assert l.find(1) is None
    assert l.head.value == 2

    # remove from middle
    assert l.remove(3) == 3
    assert l.find(3) is None

    # remove from end
    assert l.remove(4) == 4
    assert l.find(4) is None

    assert l.remove(2) == 2
    assert l.find(2) is None
    assert l.length == 0
    assert l.head is None
    assert l.tail is None