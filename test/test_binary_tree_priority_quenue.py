import unittest
from src.binary_tree_priority_queue import PriorityQueue, Node


class TestPriorityQueue(unittest.TestCase):
    def setUp(self):
        self.pq = PriorityQueue()
        self.pq.insert(50, 5)
        self.pq.insert(80, 8)
        self.pq.insert(60, 10)
        self.pq.insert(40, 4)
        self.pq.insert(20, 2)

    def test_remove_max(self):
        self.assertEqual(self.pq.remove_max(), 60)
        self.assertEqual(self.pq.remove_max(), 80)
        self.assertEqual(self.pq.remove_max(), 50)
        self.assertEqual(self.pq.remove_max(), 40)
        self.assertEqual(self.pq.remove_max(), 20)
        self.assertIsNone(self.pq.remove_max())

    def test_find_max(self):
        self.assertEqual(self.pq.find_max().value, 60)
        self.assertEqual(self.pq.find_max().priority, 10)
        self.pq.remove_max()
        self.assertEqual(self.pq.find_max().value, 80)
        self.assertEqual(self.pq.find_max().priority, 8)


if __name__ == '__main__':
    unittest.main()
