import os
import unittest
from cmath import inf

from DiGraph import DiGraph
from GraphAlgo import GraphAlgo


def graph_generator(n):
    g: DiGraph = DiGraph()
    for i in range(n):
        g.add_node(i)
        if i != 0:
            g.add_edge(i - 1, i, i)
    return g


class TestGraphAlgo(unittest.TestCase):
    def test_get_graph(self):
        g = graph_generator(5)
        g_algo = GraphAlgo(g)
        self.assertEqual(g_algo.get_graph(), g)

    def test_load_save(self):
        g = graph_generator(5)
        g_algo = GraphAlgo(g)
        file = "../TestSave.json"
        g_algo.save_to_json(file)
        new_algo = GraphAlgo()
        self.assertEqual(new_algo.load_from_json(file), True)
        for i in range(5):
            self.assertEqual(new_algo.get_graph().all_in_edges_of_node(i), g.all_in_edges_of_node(i))
            self.assertEqual(new_algo.get_graph().all_out_edges_of_node(i), g.all_out_edges_of_node(i))

    def test_shortest_path(self):
        g = graph_generator(5)
        g.add_edge(0, 4, 100)
        sp = (10, [0, 1, 2, 3, 4])
        g_algo = GraphAlgo(g)
        spa = g_algo.shortest_path(0, 4)
        self.assertEqual(sp, spa)
        sp = (float('inf'), [])
        spa = g_algo.shortest_path(4, 0)
        self.assertEqual(sp, spa)
        self.assertEqual(sp, spa)

    def test_TSP(self):
        script_dir = os.path.dirname(__file__)
        rel_path = "../data/TspTest.json"
        abs_file_path = os.path.join(script_dir, rel_path)
        my_graph_algo = GraphAlgo()
        my_graph_algo.load_from_json(abs_file_path)
        list_node, overall_distance = my_graph_algo.TSP([1, 2, 3])
        print(overall_distance)
        print(list_node)
        self.assertEqual(2, 2)
        self.assertEqual(list_node, [1, 2, 3])

    def test_center(self):
        script_dir = os.path.dirname(__file__)

        rel_path = "../data/CenterTest1.json"
        abs_file_path = os.path.join(script_dir, rel_path)
        ga = GraphAlgo()
        ga.load_from_json(abs_file_path)
        list_node, first_overall_distance = ga.centerPoint()
        print(first_overall_distance)
        print(list_node)
        self.assertEqual(first_overall_distance, 1)
        self.assertEqual(list_node, 0)

        rel_path2 = "../data/CenterTest2.json"
        abs_file_path2 = os.path.join(script_dir, rel_path2)
        ga2 = GraphAlgo()
        ga2.load_from_json(abs_file_path2)
        list_node2, second_overall_distance = ga2.centerPoint()
        print(second_overall_distance)
        print(list_node2)
        self.assertEqual(second_overall_distance, inf)
        self.assertEqual(list_node2, 0)

        rel_path3 = "../data/CenterTest3.json"
        abs_file_path3 = os.path.join(script_dir, rel_path3)
        ga3 = GraphAlgo()
        ga3.load_from_json(abs_file_path3)
        list_node3, third_overall_distance = ga3.centerPoint()
        print(third_overall_distance)
        print(list_node3)
        self.assertEqual(third_overall_distance, 3.0)
        self.assertEqual(list_node3, 0)


if __name__ == '__main__':
    unittest.main()
