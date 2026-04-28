first_maze = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 3],
    [1, 0, 1, 0, 1, 0, 1],
    [0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 2, 1, 0, 1, 0, 1],
]


mapDir = {"N": (-1, 0), "S": (1, 0), "E": (0, 1), "W": (0, -1)}
print(mapDir["N"])


def find_starting_point(maze):
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == 2:
                return [y, x]


def walk(maze, directions, position):
    for dir in directions:
        (move_y, move_x) = mapDir[dir]
        position[0] += move_y
        position[1] += move_x

        coordinate_y = position[0]
        coordinate_x = position[1]

        height = len(maze)
        width = len(maze[0])

        if coordinate_y >= height or coordinate_y < 0:
            return "Dead"

        if coordinate_x >= width or coordinate_x < 0:
            return "Dead"

        currentPosition = maze[coordinate_y][coordinate_x]

        if currentPosition == 3:
            return "Finish"

        if currentPosition == 1:
            return "Dead"

    return "Lost"


def maze_runner(maze, directions):
    position = find_starting_point(maze)
    result = walk(maze, directions, position)
    return result


maze_runner(first_maze, ["N", "N", "N", "N", "N", "E", "E", "E", "E", "E"])
