from typing import TypeVar, Generic

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self):
        self.top = None
        self.mins = None
    
    def pop(self) -> T or None:
        if self.top is None:
            return

        data = self.top.data

        if data == self.min():
            self.mins = self.mins.next     

        self.top = self.top.next

        return data

    def push(self, data: T) -> None:
        self.top = Node(data, self.top)

        if self.mins is None:
            self.mins = Node(data)
        else:
            if data <= self.mins.data:
                self.mins = Node(data, self.mins)

    def peek(self) -> T or None:
        if self.top is None:
            return
        
        return self.top.data

    def is_empty(self) -> bool:
        return self.top is None

    def min(self) -> T:
        if self.mins is None:
            return
        
        return self.mins.data


class Node(Generic[T]):
    def __init__(self, data: T, next=None):
        self.data = data
        self.next = next
