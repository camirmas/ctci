class ArrayList:
    """A dynamically resizing Array."""
    def __init__(self):
        self.items = [None, None]
        self.current = 0
        self.length = 0
        self.max = 2

    def add(self, item):
        if self.length == self.max:
            self.max *= 2
            new_l = [None]*self.max

            for idx, i in enumerate(self.items):
                new_l[idx] = i

            self.items = new_l

        self.items[self.current] = item
        self.current += 1 
        self.length += 1

    def get(self, idx: int):
        return self.items[idx]

    def remove(self, idx: int):
        item = self.items[idx]
        left = self.items[:idx]
        right = self.items[idx+1:]
        right.append(None)
        self.items = left + right
        self.length -= 1

        return item

    def contains(self, item):
        for i in self.items:
            if item == i:
                return True

        return False