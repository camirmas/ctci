from ctci.stack import Stack
from typing import TypeVar, Generic

T = TypeVar('T')

class SetOfStacks(Generic[T]):
    def __init__(self, capacity: int):
        self.stacks = []
        self.current_stack = None
        self.capacity = capacity

    def push(self, data: T):
        if self.current_stack is None:
            new_stack = Stack()
            self.stacks.append(new_stack)
            self.current_stack = new_stack
            self.current_stack.push(data)
        elif self.current_stack.length == self.capacity:
            new_stack = Stack()
            self.stacks.append(new_stack)
            self.current_stack = new_stack
            self.current_stack.push(data)
        else:
            self.current_stack.push(data)

    def pop(self) -> T or None:
        if self.current_stack is None:
            return None

        data = self.current_stack.pop()

        if self.current_stack.is_empty():
            self.stacks.pop()
            if len(self.stacks) == 0:
                self.current_stack = None
            else:
                self.current_stack = self.stacks[-1]

        return data
