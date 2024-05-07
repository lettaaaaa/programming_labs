def find_parent(parent, node_index):

    if parent[node_index] == node_index:
        return node_index
    return find_parent(parent, parent[node_index])


def union(parent, rank, island1, island2):


    xroot = find_parent(parent, island1)
    yroot = find_parent(parent, island2)

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1


def kruskal(graph):
    mst = []
    current_edge_index, edges_added = 0, 0
    parent = []
    rank = []

    for node in range(len(graph)):
        parent.append(node)
        rank.append(0)

    edges = sorted(graph, key=lambda item: item[2])

    while edges_added < len(graph) - 1 and current_edge_index < len(graph) - 1:

        island1_index, island2_index, distance = edges[current_edge_index]
        current_edge_index += 1
        x = find_parent(parent, island1_index)
        y = find_parent(parent, island2_index)

        if x != y:
            edges_added += 1
            mst.append([island1_index, island2_index, distance])
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
