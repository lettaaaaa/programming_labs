def count_islands(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = []
    islands_count = 0

    def dfs(y, x):
        if y < 0 or y >= rows or x < 0 or x >= cols or grid[y][x] == '0' or (y, x) in visited:
            return

        visited.append((y, x))
        dfs(y - 1, x - 1)
        dfs(y - 1, x)
        dfs(y - 1, x + 1)
        dfs(y + 1, x)
        dfs(y + 1, x - 1)
        dfs(y, x - 1)
        dfs(y, x + 1)
        dfs(y + 1, x + 1)

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1' and (i, j) not in visited:
                dfs(i, j)
                islands_count += 1

    return islands_count


"""
# Приклад використання
grid = [
    ['1', '1', '0', '0', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '0', '0', '0'],
    ['0', '0', '0', '1', '1']
]

print(count_islands(grid))"""
