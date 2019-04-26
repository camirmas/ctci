"""
Given a directed graph, design an algorithm to find out whether there is a
route between two nodes.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.visited = False


class Graph:
    def __init__(self):
        self.nodes = []

    def get_nodes(self) -> list:
        all_nodes = []

        q = [n for n in self.nodes]

        while q:
            node = q.pop()

            all_nodes.append(node)
            q += node.children

        return all_nodes
        
    def route_exists(self, start: Node, target: Node) -> bool:
        for node in self.get_nodes():
            node.visited = False

        q = [start]

        while len(q) > 0:
            node = q.pop()
            node.visited = True

            if node == target:
                return True
            
            for child in node.children:
                if not child.visited:
                    q.append(child)

        return False
