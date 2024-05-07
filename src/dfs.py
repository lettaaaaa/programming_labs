def find_disconnected_cities(cities, storages, pipelines):
    global keys, visited
    keys = [x[0] for x in pipelines]
    visited = set()

    for storage in storages:
        dfs(storage, pipelines)

    disconnected_cities = [city for city in cities if city not in visited]

    return disconnected_cities if disconnected_cities else []


def dfs(current, pipelines):
    if current not in visited:
        visited.add(current)
    for index in range(len(keys)):
        if keys[index] == current:
            dfs(pipelines[index][1], pipelines)
    return


# Приклад використання
"""
cities = ['Львів', 'Стрий', 'Дніпро', 'Тернопіль', 'Полтава', 'Ровно', 'Краматорськ']
storages = ['Газосховище "Донбасс"', 'Сховище_2']
pipelines = [['Газосховище "Донбасс"', 'Львів'], ['Львів', 'Стрий'], ['Газосховище "Донбасс"', 'Дніпро'],
             ['Львів', 'Полтава'], ['Стрий', 'Тернопіль'], ['Дніпро', 'Ровно']]

print(find_disconnected_cities(cities, storages, pipelines))"""
