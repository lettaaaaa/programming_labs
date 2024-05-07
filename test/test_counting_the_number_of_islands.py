import unittest
from src.counting_the_number_of_islands import count_islands


class TestCountIslands(unittest.TestCase):
    def test_empty_grid(self):
        grid = [
            ['0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0']
        ]
        self.assertEqual(count_islands(grid), 0)

    def test_all_ones(self):
        grid = [
            ['1', '1', '1', '1', '1'],
            ['1', '1', '1', '1', '1'],
            ['1', '1', '1', '1', '1'],
            ['1', '1', '1', '1', '1']
        ]
        self.assertEqual(count_islands(grid), 1)

    def test_all_zeros(self):
        grid = [
            ['0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0']
        ]
        self.assertEqual(count_islands(grid), 0)

    def test_multiple_islands(self):
        grid = [
            ['1', '1', '0', '0', '0'],
            ['1', '1', '0', '0', '1'],
            ['0', '0', '1', '0', '1'],
            ['0', '0', '0', '1', '1']
        ]
        self.assertEqual(count_islands(grid), 1)

    def test_single_island(self):
        grid = [
            ['0', '0', '0', '0', '0'],
            ['0', '1', '1', '0', '0'],
            ['0', '1', '1', '0', '0'],
            ['0', '0', '0', '0', '0']
        ]
        self.assertEqual(count_islands(grid), 1)

    def test_irregular_islands(self):
        grid = [
            ['1', '0', '1', '1', '0'],
            ['1', '0', '1', '0', '1'],
            ['0', '1', '0', '1', '0'],
            ['1', '0', '1', '0', '1']
        ]
        self.assertEqual(count_islands(grid), 1)


if __name__ == '__main__':
    unittest.main()
