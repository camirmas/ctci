from typing import TypeVar, Generic

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self):
        self.top = None
    
    def pop(self) -> T or None:
        if self.top is None:
            return

        data = self.top.data

        self.top = self.top.next

        return data

    def push(self, data: T) -> None:
        self.top = Node(data, self.top)

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
