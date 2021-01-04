# An alternative to the code presented in the lesson, for finding the shortest route length

def search_longest_path(my_grid: list[list[int]], my_init: list[int], my_goal: list[int]):
    length = 1

    print(my_grid)


if __name__ == '__main__':
    grid = [[0, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 1, 1, 1, 0],
            [0, 0, 0, 0, 1, 0]]

    init = [0, 0]
    goal = [len(grid) - 1, len(grid[0]) - 1]
    search_longest_path(grid, init, goal)
