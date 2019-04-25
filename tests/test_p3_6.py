from ctci.p3_6 import PetManager

def test_pet_manager():
    m = PetManager()

    m.enqueue("cat")
    m.enqueue("dog")

    assert m.dequeue_cat() == ("cat", 0)
    assert m.dequeue_dog() == ("dog", 1)

    m.enqueue("dog")
    m.enqueue("cat")
    m.enqueue("dog")

    assert m.dequeue_any() == ("dog", 2)
    assert m.dequeue_any() == ("cat", 3)
    assert m.dequeue_any() == ("dog", 4)
    assert m.dequeue_any() == None
