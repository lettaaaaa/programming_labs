import unittest
from src.searching_for_numbers_in_an_array import find_triplet_sum


class TestFindTripletSum(unittest.TestCase):
    def test_empty_list(self):
        self.assertFalse(find_triplet_sum([], 0))

    def test_single_element(self):
        self.assertFalse(find_triplet_sum([1], 3))

    def test_two_elements(self):
        self.assertFalse(find_triplet_sum([1, 2], 5))

    def test_triplet_found(self):
        self.assertTrue(find_triplet_sum([1, 2, 3, 4, 5], 8))

    def test_triplet_not_found(self):
        self.assertFalse(find_triplet_sum([1, 2, 3, 4, 5], 20))

    def test_negative_numbers(self):
        self.assertTrue(find_triplet_sum([-1, 0, 1, 2], 1))

    def test_duplicate_numbers(self):
        self.assertTrue(find_triplet_sum([1, 1, 2, 3, 4], 6))


if __name__ == '__main__':
    unittest.main()
