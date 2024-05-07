def find_parent(parent, i):
    # ЗАМІНИТИ: змінна i - на node_index, щоб було зрозуміліше, що це індекс вузла
    if parent[i] == i:
        return i
    return find_parent(parent, parent[i])


def union(parent, rank, x, y):
    # ЗАМІНИТИ назви змінних x та y на більш зрозумілі island1 та island2,

    xroot = find_parent(parent, x)
    yroot = find_parent(parent, y)

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1


def kruskal(graph):
    mst = []
    i, e = 0, 0
    parent = []
    rank = []

    for node in range(len(graph)):
        parent.append(node)
        rank.append(0)

    edges = sorted(graph, key=lambda item: item[2])

    while e < len(graph) - 1 and i < len(graph) - 1:
        # ЗАМІНИТИ назви змінних u, v, w на більш зрозумілі, наприклад, island1_index, island2_index, distance,

        u, v, w = edges[i]
        i += 1
        x = find_parent(parent, u)
        y = find_parent(parent, v)

        if x != y:
            e += 1
            mst.append([u, v, w])
            union(parent, rank, x, y)

    return mst


def read_graph_from_csv(filename):
    graph = []
    with open(filename, 'r') as file:
        for i, row in enumerate(file):
            row = row.strip().split(',')
            print(row)
            for j, weight in enumerate(row):
                if weight != '0' and i != j:
                    graph.append([i, j, int(weight)])
    return graph


"""
# Приклад використання
graph = read_graph_from_csv('resources/islands.csv')
print(graph)
mst = kruskal(graph)

total_weight = sum(edge[2] for edge in mst)
print(f"Мінімальна довжина підводних кабелів: {total_weight}")"""
