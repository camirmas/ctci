from typing import TypeVar, Generic

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self):
        self.top = None
        self.length = 0
    
    def pop(self) -> T or None:
        if self.top is None:
            return

        data = self.top.data
        self.top = self.top.next
        self.length -= 1

        return data

    def push(self, data: T) -> None:
        self.top = Node(data, self.top)
        self.length += 1

    def peek(self) -> T or None:
        if self.top is None:
            return
        
        return self.top.data

    def is_empty(self) -> bool:
        return self.top is None

class Node(Generic[T]):
    def __init__(self, data: T, next=None):
        self.data = data
        self.next = next
