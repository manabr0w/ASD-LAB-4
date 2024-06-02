import random
import math


def print_matrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])


def create_directed_matrix(seed, length, k):
    random.seed(seed)
    matrix = [[random.uniform(0, 2) for _ in range(length)] for _ in range(length)]
    direct_matrix = [[math.floor(matrix[i][j] * k) for j in range(length)] for i in range(length)]
    return direct_matrix


def get_vertex_power(matrix, is_direct):
    powers = []
    n = len(matrix)
    for i in range(n):
        power = 0
        for j in range(n):
            if matrix[i][j]:
                power += 1
                if not is_direct:
                    if i == j:
                        power += 1
            if is_direct:
                if matrix[j][i]:
                    power += 1
        powers.append(power)
    return powers


def print_half_power_vertex(matrix):
    n = len(matrix)
    for i in range(n):
        entry = 0
        exit = 0
        for j in range(n):
            if matrix[i][j]:
                exit += 1
            if matrix[j][i]:
                entry += 1
        print(f'VERTEX {i + 1} entry power = {entry} exit power = {exit}')


def print_homo_iso_hang_vertex(powers):
    iso = 0
    hang = 0
    for i in range(len(powers)):
        if not powers[i]:
            iso += 1
            print(f'VERTEX {i + 1} isolated')
        if powers[i] == 1:
            hang += 1
            print(f'VERTEX {i + 1} hanged')
    if not iso:
        print('No isolated vertices found')
    if not hang:
        print('No hanged vertices found')
    if all(power == powers[0] for power in powers):
        print(f'Graph is homogeneous power of {powers[0]}')
    else:
        print('Graph is not homogeneous')


def multiply_matrixes(a, b):
    n = len(a)
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += a[i][k] * b[k][j]
    return result


def get_power_matrix(matrix, power):
    n = len(matrix)
    powered_matrix = [[0 if row != col else 1 for col in range(n)] for row in range(n)]
    while power > 0:
        if power % 2 == 1:
            powered_matrix = multiply_matrixes(powered_matrix, matrix)
        matrix = multiply_matrixes(matrix, matrix)
        power //= 2
    return powered_matrix


def add_matrices(a, b):
    n = len(a)
    return [[a[i][j] + b[i][j] for j in range(n)] for i in range(n)]


def get_identity_matrix(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


def transform_bool(matrix):
    n = len(matrix)
    return [[1 if matrix[i][j] else 0 for j in range(n)] for i in range(n)]


def multiply_matrices_by_element(a, b):
    n = len(a)
    return [[a[i][j] * b[i][j] for j in range(n)] for i in range(n)]


def get_transpose_matrix(matrix):
    return [list(row) for row in zip(*matrix)]


def find_paths_from_powers(matrix, power):
    n = len(matrix)
    matrix_power = get_power_matrix(matrix, power)

    paths = []
    if power == 2:
        for i in range(n):
            for j in range(n):
                if matrix_power[i][j] > 0:
                    for k in range(n):
                        if matrix[i][k] > 0 and matrix[k][j] > 0:
                            paths.append([i + 1, k + 1, j + 1])
    elif power == 3:
        for i in range(n):
            for j in range(n):
                if matrix_power[i][j] > 0:
                    for k in range(n):
                        if matrix[i][k] > 0:
                            for x in range(n):
                                if matrix[k][x] > 0 and matrix[x][j] > 0:
                                    paths.append([i + 1, k + 1, x + 1, j + 1])

    return paths


def print_paths_of_vertexes(matrix):
    pathslen2 = find_paths_from_powers(matrix, 2)
    pathslen3 = find_paths_from_powers(matrix, 3)

    print('\nPaths of length 2:')
    for path in pathslen2:
        print(path)

    print('\nPaths of length 3:')
    for path in pathslen3:
        print(path)


def get_reachability_matrix(matrix):
    n = len(matrix)
    reachability_matrix = matrix
    for i in range(2, n - 1):
        reachability_matrix = add_matrices(reachability_matrix, get_power_matrix(matrix, i))
    reachability_matrix = add_matrices(reachability_matrix, get_identity_matrix(n))
    reachability_matrix = transform_bool(reachability_matrix)
    return reachability_matrix


def get_strong_connectivity_matrix(reachability_matrix):
    return multiply_matrices_by_element(reachability_matrix, get_transpose_matrix(reachability_matrix))


def dfs(strong_connectivity_matrix, vertex, component, is_visited):
    n = len(strong_connectivity_matrix)
    component[vertex] = 1
    is_visited[vertex] = True
    for i in range(n):
        if (not is_visited[i]) and strong_connectivity_matrix[vertex][i]:
            dfs(strong_connectivity_matrix, i, component, is_visited)


def get_strong_connectivity_components(strong_connectivity_matrix):
    n = len(strong_connectivity_matrix)
    is_visited = [False] * n
    components_matrix = [[0 for _ in range(n)] for _ in range(n)]

    for vertex in range(n):
        if not is_visited[vertex]:
            dfs(strong_connectivity_matrix, vertex, components_matrix[vertex], is_visited)

    strong_connectivity_components = []
    for i in range(len(components_matrix)):
        temp = []
        if components_matrix[i][i]:
            for j in range(len(components_matrix[i])):
                if components_matrix[i][j]:
                    temp.append(j + 1)
            strong_connectivity_components.append(temp)

    return strong_connectivity_components
