class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def find(self, item):
        if self.head is None:
            return None
        return self.head.find(item)

    def find_by(self, fn):
        if self.head is None:
            return None
        return self.head.find_by(fn)

    def append(self, item):
        if self.head is None:
            l = LinkedListNode(item)
            self.head = l
            self.tail = l
        else:
            self.tail.append(item)
            self.tail = self.tail.next

        self.length += 1

    def remove(self, item):
        node = self.find(item)

        if node is None:
            return None

        if node == self.head:
            if self.head == self.tail:
                self.tail = self.head.next
            self.head = self.head.next
        else:
            predecessor = self.head.find_predecessor(node)
            if node == self.tail:
                self.tail = predecessor

            predecessor.next = node.next

        self.length -= 1

        return item


class LinkedListNode:
    def __init__(self, item):
        self.value = item
        self.next = None

    def find(self, item):
        if self == None:
            return None

        if self.value == item:
            return self

        if self.next is None:
            return None

        return self.next.find(item)

    def find_by(self, fn):
        if self == None:
            return None

        if fn(self.value):
            return self

        if self.next is None:
            return None

        return self.next.find(fn)

    def find_predecessor(self, node):
        if self.next is None:
            return None

        if self.next == node:
            return self

        return self.next.find_predecessor(node)

    def append(self, item):
        self.next = LinkedListNode(item)