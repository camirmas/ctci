from ctci.queue import Queue

class PetManager:
    def __init__(self):
        self.cats = Queue()
        self.dogs = Queue()
        self.counter = 0

    def enqueue(self, animal: str): 
        assert animal == "cat" or animal == "dog"

        if animal == "cat":
            self.cats.add(("cat", self.counter))
        else:
            self.dogs.add(("dog", self.counter))

        self.counter += 1

    def dequeue_cat(self) -> (str, int) or None:
        return self.cats.remove()

    def dequeue_dog(self) -> (str, int) or None:
        return self.dogs.remove()

    def dequeue_any(self) -> (str, int) or None:
        if self.cats.is_empty():
            return self.dogs.remove()

        if self.dogs.is_empty():
            return self.cats.remove()

        _, cat_n = self.cats.peek()
        _, dog_n = self.dogs.peek()

        if cat_n < dog_n:
            return self.cats.remove()
        else:
            return self.dogs.remove()
