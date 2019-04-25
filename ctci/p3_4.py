from ctci.stack import Stack

class MyQueue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def add(self, data):
        self.s1.push(data)

    def remove(self):
        if self.is_empty():
            return

        if not self.s2.is_empty():
            return self.s2.pop()

        current = self.s1.pop()
        while not self.s1.is_empty():
            self.s2.push(current)
            current = self.s1.pop()

        return current

    def is_empty(self):
        return self.s1.is_empty() and self.s2.is_empty()
