import unittest
from src.search_for_k_element import ElementK


class TestElementK(unittest.TestCase):
    def test_1(self):
        Test1 = ElementK([15, 7, 22, 9, 36, 2, 42, 18], 3)
        self.assertEqual((Test1.element_k, Test1.pos_k), (22, 2))

    def test_2(self):
        Test2 = ElementK([21, 2, 5, 90, 5, 78, 4, 3], 1)
        self.assertEqual((Test2.element_k, Test2.pos_k), (90, 3))

    def test_3(self):
        Test3 = ElementK([5, 9, 45, 76, 2, 0, 6, 8], 2)
        self.assertEqual((Test3.element_k, Test3.pos_k), (45, 2))


if __name__ == "__main__":
    unittest.main()
