"""Describe how you could use a single array to implement three stacks."""
class StackManager:
    def __init__(self):
        self.stacks = []
        self.top = {
            1: None,
            2: None,
            3: None,
        }
        self.length = {
            1: 0,
            2: 0,
            3: 0,
        }

    def push(self, stack: int, data):
        assert stack in self.top

        if stack == 1:
            if self.top[1] is not None:
                self.top[1] += 1
                
                if self.top[2] is not None:
                    self.top[2] += 1
                
                if self.top[3] is not None:
                    self.top[3] += 1
            else:
                self.top[1] = 0

        elif stack == 2:
            if self.top[2] is not None:
                self.top[2] += 1

                if self.top[3] is not None:
                    self.top[3] += 1
            else:
                if self.top[1] is not None:
                    self.top[2] = self.top[1] + 1
                else:
                    self.top[2] = 0

        else:
            if self.top[3] is not None:
                self.top[3] += 1
            else:
                self.top[3] = len(self.stacks)

        self.stacks.insert(self.top[stack], data)
        self.length[stack] += 1

    def pop(self, stack: int):
        assert stack in self.top

        if self.top[stack] is None:
            return None

        top = self.stacks.pop(self.top[stack])
        self.top[stack] -= 1
        self.length[stack] -= 1

        if self.length[stack] == 0:
            self.top[stack] = None

        if stack == 1:
            if self.top[2] is not None:
                self.top[2] -= 1

            if self.top[3] is not None:
                self.top[3] -= 1

        elif stack == 2:
            if self.top[3] is not None:
                self.top[3] -= 1

        return top
