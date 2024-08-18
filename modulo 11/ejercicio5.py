def dfs(grid, i, j, a, b):
    if i < 0 or i >= a or j < 0 or j >= b or grid[i][j] != 'X':
        return 0

    grid[i][j] = '.'
    size = 1

    size += dfs(grid, i - 1, j, a, b)
    size += dfs(grid, i + 1, j, a, b)
    size += dfs(grid, i, j - 1, a, b)
    size += dfs(grid, i, j + 1, a, b)
    return size


def max_forested_area(grid):
    a = len(grid)
    b = len(grid[0])
    max_area = 0

    for i in range(a):
        for j in range(b):
            if grid[i][j] == 'X':
                area = dfs(grid, i, j, a, b)
                max_area = max(max_area, area)
    return max_area


for _ in range(int(input())):
    A, B = tuple(map(int, input().split()))
    forest = []
    for _ in range(A):
        row = input()
        forest.append(list(row))
    print(max_forested_area(forest))
