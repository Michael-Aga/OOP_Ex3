import json
import math
from typing import List
import heapq
import matplotlib.pyplot as plt
from src.GraphAlgoInterface import GraphAlgoInterface
from src.DiGraph import DiGraph
import random


class GraphAlgo(GraphAlgoInterface, DiGraph):

    def __init__(self, graph: DiGraph = None):
        """ init """
        super().__init__()
        self.my_graph = graph

    def get_graph(self):
        """ :returns the graph that we preforms the algorithms on """
        return self.my_graph

    def load_from_json(self, file_name: str) -> bool:
        """
        loads a graph from json
        :returns true if successfully loaded else false
        """
        self.my_graph = DiGraph()
        try:
            with open(file_name, "r") as file:
                jsondict = json.load(file)

                for node in jsondict["Nodes"]:
                    if "pos" in node:
                        i = 0
                        pos = ()

                        for position in node["pos"].split(','):
                            pos = pos + (float(position),)
                        self.my_graph.add_node(node_id=node["id"], pos=pos)

                    else:
                        self.my_graph.add_node(node_id=node["id"])

                for edge in jsondict["Edges"]:
                    self.my_graph.add_edge(id1=edge["src"], id2=edge["dest"], weight=edge["w"])

            return True

        except IOError as e:
            print(e)
            return False

    def save_to_json(self, file_name: str) -> bool:
        """
        saves a graph to json
        :returns true if successfully saved else false
        """
        nodes = []
        edges = []

        for node in self.my_graph.get_all_v():
            if self.my_graph.get_all_v()[node].get_pos() is not None:
                pos = str(self.my_graph.get_all_v()[node].get_pos())
                nodes.append({"id": node, "pos": pos})

            else:
                nodes.append({"id": node})

            for edge in self.my_graph.all_out_edges_of_node(node):
                edges.append({"src": node, "dest": edge, "w": self.my_graph.get_all_v()[node].get_weight(edge)})
        jsondict = {"Nodes": nodes, "Edges": edges}

        try:
            with open(file_name, "w") as file:
                json.dump(jsondict, fp=file)
                return True

        except IOError as e:
            print(e)
            return False

        pass

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        finds the shortest path between two nodes
        :returns the distance and a list of the path itself (list of integers that represent nodes)
        """
        if self.my_graph is None:
            return float('inf'), []

        for node in self.my_graph.get_all_v():
            self.my_graph.get_all_v()[node].set_distance("inf")
            self.my_graph.get_all_v()[node].set_previous_node(None)

        if id1 not in self.my_graph.get_all_v() or id2 not in self.my_graph.get_all_v():
            return float('inf'), []

        distance = 0
        self.my_graph.get_all_v()[id1].set_distance(distance)
        hq = []
        heapq.heappush(hq, self.my_graph.get_all_v()[id1])

        while len(hq):
            node = heapq.heappop(hq)
            distance = self.my_graph.get_all_v()[node.get_id()].get_distance()

            for node2 in self.my_graph.all_out_edges_of_node(node.get_id()):
                new_distance = distance + self.my_graph.get_all_v()[node.get_id()].get_weight(node2)

                if self.my_graph.get_all_v()[node2].get_distance() == "inf":
                    self.my_graph.get_all_v()[node2].set_distance(new_distance)
                    self.my_graph.get_all_v()[node2].set_previous_node(node)
                    heapq.heappush(hq, self.my_graph.get_all_v()[node2])

                elif new_distance < self.my_graph.get_all_v()[node2].get_distance():
                    self.my_graph.get_all_v()[node2].set_distance(new_distance)
                    self.my_graph.get_all_v()[node2].set_previous_node(node)
                    heapq.heappush(hq, self.my_graph.get_all_v()[node2])

        if self.my_graph.get_all_v()[id2].get_distance() == "inf":
            return float('inf'), []

        else:
            my_list = []
            my_list.insert(0, id2)
            _id = self.my_graph.get_all_v()[id2].get_previous_node()

            while _id is not None:
                my_list.insert(0, _id.get_id())
                _id = self.my_graph.get_all_v()[_id.get_id()].get_previous_node()

            return self.my_graph.get_all_v()[id2].get_distance(), my_list

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        """
        Finds the shortest path that visits all the nodes in the list
        :param node_lst: A list of nodes id's
        :return: A list of the nodes id's in the path, and the overall distance
        """
        best_tsp = []
        overall_distance = 0

        while len(node_lst) > 1:
            path = self.shortest_path(node_lst[0], node_lst[1])
            best_tsp += path[1]
            overall_distance += path[0]
            best_tsp.pop()

            for i in node_lst:
                if i in best_tsp:
                    node_lst.remove(i)

        best_tsp.append(node_lst.pop())

        return best_tsp, overall_distance

    def centerPoint(self) -> (int, float):
        """
        Finds the node that has the shortest distance to it's farthest node.
        :return: The nodes id, min-maximum distance
        """
        nodes_id = 0
        min_maximum_distance = math.inf
        nodes = self.my_graph.get_all_v()

        for node in nodes.values():
            src = node.get_id()
            shortest_path_found = 0
            nodes_again = self.my_graph.get_all_v()

            for dest in nodes_again.values():
                if dest != node:
                    check_path = self.shortest_path(src, dest.get_id())
                    destination = check_path[0]

                    if destination > shortest_path_found:
                        shortest_path_found = destination

            if shortest_path_found < min_maximum_distance:
                min_maximum_distance = shortest_path_found
                nodes_id = src

        return nodes_id, min_maximum_distance

    def plot_graph(self) -> None:
        """ Plots the graph """
        x_val = []
        y_val = []

        for node in self.my_graph.get_all_v():
            if self.my_graph.get_all_v()[node].get_pos() is None:
                pos = ()

                for i in range(2):
                    pos = pos + (random.random(),)

                pos = pos + (0,)
                self.my_graph.get_all_v()[node].set_pos(pos)

        ax = plt.axes()

        for node1 in self.my_graph.get_all_v():
            start_x = self.my_graph.get_all_v()[node1].get_pos()[0]
            start_y = self.my_graph.get_all_v()[node1].get_pos()[1]

            plt.annotate(node1, xy=(start_x, start_y), fontsize=12, color="green")

            x_val.append(self.my_graph.get_all_v()[node1].get_pos()[0])
            y_val.append(self.my_graph.get_all_v()[node1].get_pos()[1])

            for node2 in self.my_graph.all_out_edges_of_node(node1):
                end_x = self.my_graph.get_all_v()[node2].get_pos()[0]
                end_y = self.my_graph.get_all_v()[node2].get_pos()[1]

                ax.annotate("", xy=(start_x, start_y), xytext=(end_x, end_y), arrowprops=dict(arrowstyle="->"))

        plt.title("Graph")
        plt.plot(x_val, y_val, 'ro')
        plt.show()
