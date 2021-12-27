from src.GraphInterface import GraphInterface
from src.NodeData import Node


class DiGraph(GraphInterface):
    def __init__(self):
        self.v = {}
        self.edges_quantity = 0
        self.mc = 0

    def __repr__(self):
        return "Graph: |V|=" + len(self.v).__str__() + " , |E|=" + self.edges_quantity.__str__()

    def v_size(self) -> int:
        """ :returns the number of vertices in this graph """
        return len(self.v)

    def e_size(self) -> int:
        """ :returns the number of edges in this graph """
        return self.edges_quantity

    def get_all_v(self) -> dict:
        """ :returns a dictionary of all the nodes in the Graph, each node is represented using a pair (node_id,
        node_data) """
        return self.v

    def all_in_edges_of_node(self, id1: int) -> dict:
        """ :returns a dictionary of all the nodes connected to (into) node_id """
        if self.v.__contains__(id1):
            return self.v[id1].get_in()

    def all_out_edges_of_node(self, id1: int) -> dict:
        """ :returns a dictionary of all the nodes connected from node_id """
        if self.v.__contains__(id1):
            return self.v[id1].get_out()

    def get_mc(self) -> int:
        """ :returns the number of changes that were made in this graph """
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """ Adds an edge to the graph. """
        if id1 not in self.v or id2 not in self.v or id2 in self.v[id1].get_out() or weight < 0:
            return False
        else:
            self.v[id1].add_out(id2, weight)
            self.v[id2].add_in(id1, weight)
            self.edges_quantity += 1
            self.mc += 1
            return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        """ Adds a node to the graph """
        if not (self.v.__contains__(node_id)):
            self.v[node_id] = Node(node_id, pos)
            self.mc += 1
            return True
        else:
            return False

    def remove_node(self, node_id: int) -> bool:
        """ removes a node from the graph """
        if not (self.v.__contains__(node_id)):
            return False
        else:
            incoming_edges_copy = self.v[node_id].get_in().copy()
            self.mc -= len(self.v[node_id].get_in())

            for node in incoming_edges_copy.keys():
                self.remove_edge(node, node_id)

            self.edges_quantity -= len(self.v[node_id].get_out())
            self.v.pop(node_id)
            self.mc += 1

            return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """ removes the edge between two nodes """
        if node_id1 not in self.v or node_id2 not in self.v or node_id2 not in self.v[node_id1].get_out():
            return False
        else:
            del self.v[node_id1].get_out()[node_id2]
            del self.v[node_id2].get_in()[node_id1]
            self.edges_quantity -= 1
            self.mc += 1

            return True
