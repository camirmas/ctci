from ctci.hashtable import HashTable

def test_hashtable():
    h = HashTable(10)
    
    assert h.capacity == 10
    assert h.items == [None]*10

def test_hashtable_insert():
    h = HashTable(10)
    h.insert("stuff", 1)

def test_hashtable_get():
    h = HashTable(10)
    h.insert("stuff", 1)
    assert h.get("stuff") == 1

def test_hashtable_overwrite():
    h = HashTable(10)
    h.insert("stuff", 1)
    assert h.get("stuff") == 1

    h.insert("stuff", 2)

    assert h.get("stuff") == 2

def test_hashtable_delete():
    h = HashTable(10)
    h.insert("stuff", 1)

    assert h.delete("stuff") == 1
    assert h.get("stuff") is None