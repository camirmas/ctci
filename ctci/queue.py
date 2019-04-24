from typing import TypeVar, Generic

T = TypeVar('T')

class Queue(Generic[T]):
    def __init__(self):
        self.first = None
        self.last = None

    def add(self, data: T):
        node = Node(data)

        if self.is_empty():
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node

    def remove(self) -> T or None:
        if self.first is None:
            return None

        first = self.first
        self.first = self.first.next

        return first.data

    def peek(self) -> T or None:
        if self.first is None:
            return None

        return self.first.data

    def is_empty(self) -> bool:
        return self.first is None


class Node(Generic[T]):
    def __init__(self, data: T):
        self.data = data
        self.next = None
