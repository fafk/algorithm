"""


As a part of the route planner, the route_exists method is used as a quick filter if the destination
is reachable, before using more computationally intensive procedures for finding the optimal route.

The roads on the map are rasterized and produce a matrix of boolean values - True if the road is
 present or False if it is not. The roads in the matrix are connected only if the road is immediately left, right, below or above it.

Finish the route_exists method so that it returns True if the destination is reachable or False if
it is not. The from_row and from_column parameters are the starting row and column in the map_matrix.
The to_row and to_column are the destination row and column in the map_matrix.
The map_matrix parameter is the above mentioned matrix produced from the map.

For example, the following code should return True since destination is reachable:

map_matrix = [
    [True, False, False],
    [True, True, False],
    [False, True, True]
];

route_exists(0, 0, 2, 2, map_matrix)
"""


def route_exists_rec(from_row, from_column, to_row, to_column, map_matrix, visited={}):
    v = None
    if from_row + 1 < len(map_matrix):
        if map_matrix[from_row + 1][from_column]:
            if from_row + 1 == to_row and from_column == to_column:
                return True
            if not (from_row + 1, from_column) in visited:
                v = visited.copy() if not v else v
                v[(from_row, from_column)] = True
                if route_exists_rec(from_row + 1, from_column, to_row, to_column, map_matrix, v):
                    return True
    if from_column + 1 < len(map_matrix[0]):
        if map_matrix[from_row][from_column + 1]:
            if from_row == to_row and from_column + 1 == to_column:
                return True
            if not (from_row, from_column + 1) in visited:
                v = visited.copy() if not v else v
                v[(from_row, from_column)] = True
                if route_exists_rec(from_row, from_column + 1, to_row, to_column, map_matrix, v):
                    return True
    if from_row - 1 >= 0:
        if map_matrix[from_row - 1][from_column]:
            if from_row - 1 == to_row and from_column == to_column:
                return True
            if not (from_row - 1, from_column) in visited:
                v = visited.copy() if not v else v
                v[(from_row, from_column)] = True
                if route_exists_rec(from_row - 1, from_column, to_row, to_column, map_matrix, v):
                    return True
    if from_column - 1 >= 0:
        if map_matrix[from_row][from_column - 1]:
            if from_row == to_row and from_column - 1 == to_column:
                return True
            if not (from_row, from_column - 1) in visited:
                v = visited.copy() if not v else v
                v[(from_row, from_column)] = True
                if route_exists_rec(from_row, from_column - 1, to_row, to_column, map_matrix, v):
                    return True

    return False


visited = {}


def route_exists(from_row, from_column, to_row, to_column, map_matrix):
    if not map_matrix[from_row][from_column]:
        return False
    current = (from_row, from_column)
    stack = []
    while current:
        if current[0] == to_row and current[1] == to_column:
            return True

        visited[(current[0], current[1])] = True

        if current[0] + 1 < len(map_matrix):
            if map_matrix[current[0] + 1][current[1]]:
                if not (current[0] + 1, current[1]) in visited:
                    stack.append((current[0] + 1, current[1]))
        if current[0] - 1 >= 0:
            if map_matrix[current[0] - 1][current[1]]:
                if not (current[0] - 1, current[1]) in visited:
                    stack.append((current[0] - 1, current[1]))

        if current[1] + 1 < len(map_matrix[0]):
            if map_matrix[current[0]][current[1] + 1]:
                if not (current[0], current[1] + 1) in visited:
                    stack.append((current[0], current[1] + 1))

        if current[1] - 1 >= 0:
            if map_matrix[current[0]][current[1] - 1]:
                if not (current[0], current[1] - 1) in visited:
                    stack.append((current[0], current[1] - 1))

        current = stack.pop() if stack else None
    return False


if __name__ == '__main__':
    map_matrix = [
        [True, True, True, True, True],
        [True, False, True, False, False],
        [True, True, True, False, False],
        [False, True, False, False, False],
        [False, True, True, True, True],
    ];

    args = [0, 0, 4, 4, map_matrix]
    print(route_exists(*args))
    print(route_exists_rec(*args))
