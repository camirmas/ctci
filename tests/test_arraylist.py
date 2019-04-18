from ctci.arraylist import ArrayList

def test_arraylist():
    l = ArrayList()

    assert l.length == 0
    assert l.current == 0
    assert l.items == [None, None]
    assert l.max == 2

def test_arraylist_add():
    l = ArrayList()
    l.add(1)

    assert l.length == 1
    assert l.max == 2

    l.add(2)
    l.add(3)

    assert l.length == 3
    assert l.max == 4

    l.add(4)
    l.add(5)

    assert l.length == 5
    assert l.max == 8

def test_arraylist_get():
    l = ArrayList()

    assert l.get(0) == None

    l.add(1)

    assert l.get(0) == 1

def test_arraylist_remove():
    l = ArrayList()

    l.add(1)
    l.add(2)
    l.add(3)
    l.add(4)
    l.add(5)

    assert l.remove(4) == 5
    assert l.remove(3) == 4
    assert l.remove(2) == 3
    assert l.remove(1) == 2
    assert l.remove(0) == 1
    assert l.length == 0

def test_arraylist_contains():
    l = ArrayList()

    assert l.contains(1) == False

    l.add(1)

    assert l.contains(1)