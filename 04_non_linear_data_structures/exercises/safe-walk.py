from collections import deque


def can_reach_end_bfs(grid, health):
    m, n = len(grid), len(grid[0])

    visited = [[-1] * n for _ in range(m)]

    queue = deque()

    start_health = health - grid[0][0]

    if start_health < 1:
        return False

    queue.append((0, 0, start_health))
    visited[0][0] = start_health

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y, h = queue.popleft()

        if x == m - 1 and y == n - 1:
            return True

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < m and 0 <= ny < n:
                new_health = h - grid[nx][ny]
                if new_health >= 1 and new_health > visited[nx][ny]:
                    visited[nx][ny] = new_health
                    queue.append((nx, ny, new_health))

    return False


print(can_reach_end_bfs([[0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0]], 1))  # True
print(
    can_reach_end_bfs(
        [
            [0, 1, 1, 0, 0, 0],
            [1, 0, 1, 0, 0, 0],
            [0, 1, 1, 1, 0, 1],
            [0, 0, 1, 0, 1, 0],
        ],
        3,
    )
)  # False
print(can_reach_end_bfs([[1, 1, 1], [1, 0, 1], [1, 1, 1]], 5))  # True
