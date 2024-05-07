import unittest
from src.dfs import find_disconnected_cities


class TestDisconnectedCities(unittest.TestCase):
    def test_find_disconnected_cities(self):
        cities = ['Львів', 'Стрий', 'Дніпро', 'Тернопіль', 'Полтава', 'Ровно', 'Краматорськ']
        storages = ['Газосховище "Донбасс"', 'Сховище_2']
        pipelines = [['Газосховище "Донбасс"', 'Львів'], ['Львів', 'Стрий'], ['Газосховище "Донбасс"', 'Дніпро'],
                     ['Львів', 'Полтава'], ['Стрий', 'Тернопіль'], ['Дніпро', 'Ровно']]
        expected_output = ['Краматорськ']
        self.assertEqual(find_disconnected_cities(cities, storages, pipelines), expected_output)

    def test_find_disconnected_cities_2(self):
        cities = ['Львів', 'Стрий', 'Дніпро', 'Тернопіль', 'Полтава', 'Ровно']
        storages = ['Газосховище "Донбасс"', 'Сховище_2']
        pipelines = [['Газосховище "Донбасс"', 'Львів'], ['Львів', 'Стрий'], ['Газосховище "Донбасс"', 'Дніпро'],
                     ['Львів', 'Полтава'], ['Стрий', 'Тернопіль'], ['Дніпро', 'Ровно']]
        expected_output = []
        self.assertEqual(find_disconnected_cities(cities, storages, pipelines), expected_output)


if __name__ == '__main__':
    unittest.main()
