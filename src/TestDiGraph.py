import unittest
from src.DiGraph import DiGraph


def graph_generator(n):
    g: DiGraph = DiGraph()
    for i in range(n):
        g.add_node(i)
        if i != 0:
            g.add_edge(i - 1, i, i)
    return g


class TestDiGraph(unittest.TestCase):

    def test_v_size_e_size_mc(self):
        g = graph_generator(5)

        self.assertEqual(g.v_size(), 5)
        self.assertEqual(g.e_size(), 4)
        self.assertEqual(g.get_mc(), 9)

        g.add_node(5)

        self.assertEqual(g.v_size(), 6)
        self.assertEqual(g.get_mc(), 10)

        g.add_node(5)

        self.assertEqual(g.v_size(), 6)
        self.assertEqual(g.get_mc(), 10)

        g.add_node(6)

        self.assertEqual(g.v_size(), 7)
        self.assertEqual(g.get_mc(), 11)

        g.remove_node(3)

        self.assertEqual(g.v_size(), 6)
        self.assertEqual(g.e_size(), 2)
        self.assertEqual(g.get_mc(), 12)

        g.remove_node(3)

        self.assertEqual(g.v_size(), 6)
        self.assertEqual(g.e_size(), 2)
        self.assertEqual(g.get_mc(), 12)

        g.add_edge(2, 4, 1)

        self.assertEqual(g.v_size(), 6)
        self.assertEqual(g.e_size(), 3)
        self.assertEqual(g.get_mc(), 13)

    def test_get_all_v(self):
        g = graph_generator(5)
        self.assertEqual(len(g.get_all_v()), 5)

        g = graph_generator(10)
        self.assertEqual(len(g.get_all_v()), 10)

        g = graph_generator(20)
        self.assertEqual(len(g.get_all_v()), 20)

    def test_all_in_edges_of_node(self):
        g = graph_generator(5)
        self.assertEqual(len(g.all_in_edges_of_node(0)), 0)
        self.assertEqual(len(g.all_in_edges_of_node(1)), 1)

    def test_all_out_edges_of_node(self):
        g = graph_generator(5)
        self.assertEqual(len(g.all_out_edges_of_node(0)), 1)
        self.assertEqual(len(g.all_out_edges_of_node(4)), 0)

    def test_add_edge(self):
        g = graph_generator(5)

        self.assertEqual(g.e_size(), 4)
        for i in range(1, 5):
            g.add_edge(i, i - 1, i)

        self.assertEqual(g.e_size(), 8)
        for i in range(1, 5):
            g.add_edge(i, i - 1, i)

        self.assertEqual(g.e_size(), 8)

    def test_add_node(self):
        g = graph_generator(5)

        self.assertEqual(g.v_size(), 5)
        for i in range(5, 15):
            g.add_node(i)

        self.assertEqual(g.v_size(), 15)
        for i in range(5, 13):
            g.add_node(i)

        self.assertEqual(g.v_size(), 15)

    def test_remove_node(self):
        g = graph_generator(20)

        self.assertEqual(g.v_size(), 20)

        g.remove_node(0)

        self.assertEqual(g.v_size(), 19)

        g.remove_node(0)

        self.assertEqual(g.v_size(), 19)

        g.remove_node(1)
        self.assertEqual(g.v_size(), 18)

    def test_remove_edge(self):
        g = graph_generator(5)

        self.assertEqual(g.e_size(), 4)
        g.remove_edge(0, 1)

        self.assertEqual(g.e_size(), 3)
        g.remove_edge(0, 1)

        self.assertEqual(g.e_size(), 3)
        g.add_edge(0, 1, 1)

        self.assertEqual(g.e_size(), 4)


if __name__ == '__main__':
    unittest.main()
