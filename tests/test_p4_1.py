from ctci.p4_1 import Graph, Node

def test_graph_route_exists():
    g = Graph()

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node1.children = [node2, node3]

    node4 = Node(4)
    g.nodes.append(node1)

    assert g.route_exists(node1, node3)
    assert not g.route_exists(node1, node4)
