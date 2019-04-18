from ctci.linkedlist import LinkedList

class HashTable:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.items = [None]*capacity

    def insert(self, key, val):
        h = hash(key)
        bucket_idx = h % self.capacity
        bucket = self.items[bucket_idx]
        item = Item(key, val)

        if bucket is None:
            l = LinkedList()
            l.append(item)
            self.items[bucket_idx] = l
        else:
            node = bucket.find_by(lambda i: i.key == key)
            if node is None:
                self.items[bucket_idx].append(item)
            else:
                item = node.value
                item.value = val

    def get(self, key):
        bucket = self.get_bucket(key)

        if bucket is None:
            return None

        node = bucket.find_by(lambda item: item.key == key)
        if node is None:
            return None
        else:
            item: Item = node.value
            return item.value

    def delete(self, key):
        bucket = self.get_bucket(key)
        node = bucket.find_by(lambda item: item.key == key)

        if node is None:
            return None
        else:
            item = bucket.remove(node.value)
            if item is None:
                return None
            return item.value

    def get_bucket(self, key):
        h = hash(key)
        bucket_idx = h % self.capacity

        return self.items[bucket_idx]

class Item:
    def __init__(self, key, val):
        self.key = key
        self.value = val