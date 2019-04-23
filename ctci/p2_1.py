class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def length(self) -> int:
        if self.next is None:
            return 1
        return 1 + self.next.length()

    def to_list(self):
        def get_vals(head, vals) -> list:
            if head is None:
                return vals

            vals.append(head.val)
            return get_vals(head.next, vals)

        return get_vals(self, [])

def remove(head: Node, remove: Node) -> None:
    if head is None or remove is None:
        return None

    pred = find_predecessor(head, remove)
    pred.next = remove.next

def remove_dups(head: Node):
    nodes = set()

    current = head
    while current is not None:
        if current.val in nodes:
            remove(head, current)

        nodes.add(current.val)
        current = current.next

def find_predecessor(current: Node, target: Node) -> Node or None:
    if current is None:
        return None

    if current.next == target:
        return current

    return find_predecessor(current.next, target)
