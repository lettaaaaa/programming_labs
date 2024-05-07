import unittest
from unittest.mock import patch, mock_open
from src.search_for_minimum_length import kruskal, read_graph_from_csv


class TestMinimumLength(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open,
           read_data='0,10,5,0,15\n10,0,0,8,20\n5,0,0,6,25\n0,8,6,0,14\n15,20,25,14,0')
    def test_minimum_length(self, mock_file):
        graph = read_graph_from_csv('islands.csv')
        mst = kruskal(graph)
        total_weight = sum(edge[2] for edge in mst)
        self.assertEqual(total_weight, 33)


if __name__ == '__main__':
    unittest.main()
