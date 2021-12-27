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
        test_graph = graph_generator(5)
        my_graph_algo = GraphAlgo(test_graph)
        self.assertEqual(my_graph_algo.get_graph(), test_graph)

    def test_load_save(self):
        test_graph = graph_generator(5)
        my_graph_algo = GraphAlgo(test_graph)
        file = "../TestSave.json"
        my_graph_algo.save_to_json(file)
        new_algo = GraphAlgo()
        self.assertEqual(new_algo.load_from_json(file), True)

        for i in range(5):
            self.assertEqual(new_algo.get_graph().all_in_edges_of_node(i), test_graph.all_in_edges_of_node(i))
            self.assertEqual(new_algo.get_graph().all_out_edges_of_node(i), test_graph.all_out_edges_of_node(i))

    def test_shortest_path(self):
        my_graph = graph_generator(5)

        my_graph.add_edge(0, 4, 100)
        sp = (10, [0, 1, 2, 3, 4])
        g_algo = GraphAlgo(my_graph)
        spa = g_algo.shortest_path(0, 4)
        self.assertEqual(sp, spa)
        
        sp = (float('inf'), [])
        spa = g_algo.shortest_path(4, 0)
        self.assertEqual(sp, spa)
        self.assertEqual(sp, spa)

    def test_TSP(self):
        file_dir = os.path.dirname(__file__)
        test_file = "../data/TspTest.json"
        test_file_path = os.path.join(file_dir, test_file)
        my_graph_algo = GraphAlgo()
        my_graph_algo.load_from_json(test_file_path)
        list_of_node, overall_distance = my_graph_algo.TSP([1, 2, 3])
        print(overall_distance)
        print(list_of_node)
        self.assertEqual(2, 2)
        self.assertEqual(list_of_node, [1, 2, 3])

    def test_center(self):
        files_dir = os.path.dirname(__file__)

        test_file = "../data/CenterTest1.json"
        test_file_path = os.path.join(files_dir, test_file)
        my_graph_algo = GraphAlgo()
        my_graph_algo.load_from_json(test_file_path)
        list_of_node, first_overall_distance = my_graph_algo.centerPoint()
        print(first_overall_distance)
        print(list_of_node)
        self.assertEqual(first_overall_distance, 1)
        self.assertEqual(list_of_node, 0)

        second_test_file = "../data/CenterTest2.json"
        second_test_file_path2 = os.path.join(files_dir, second_test_file)
        my_second_graph_algo = GraphAlgo()
        my_second_graph_algo.load_from_json(second_test_file_path2)
        second_list_of_node, second_overall_distance = my_second_graph_algo.centerPoint()
        print(second_overall_distance)
        print(second_list_of_node)
        self.assertEqual(second_overall_distance, inf)
        self.assertEqual(second_list_of_node, 0)

        third_test_file = "../data/CenterTest3.json"
        third_test_file_path = os.path.join(files_dir, third_test_file)
        my_third_graph_algo = GraphAlgo()
        my_third_graph_algo.load_from_json(third_test_file_path)
        third_list_of_node, third_overall_distance = my_third_graph_algo.centerPoint()
        print(third_overall_distance)
        print(third_list_of_node)
        self.assertEqual(third_overall_distance, 3.0)
        self.assertEqual(third_list_of_node, 0)


if __name__ == '__main__':
    unittest.main()
