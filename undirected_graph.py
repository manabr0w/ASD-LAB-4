import turtle

from constants import SEED, NUM_VERTICES, K
from graph import draw_graph
from matrix_utils import print_matrix, create_directed_matrix, get_vertex_power, print_homo_iso_hang_vertex


def get_undirected_matrix(direct_matrix):
    size = len(direct_matrix)
    matrix = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            if direct_matrix[i][j]:
                matrix[i][j] = 1
                matrix[j][i] = 1
    return matrix


def main():
    directed_matrix = create_directed_matrix(SEED, NUM_VERTICES, K)
    undirected_matrix = get_undirected_matrix(directed_matrix)
    print('Undirected matrix:')
    print_matrix(undirected_matrix)

    draw_graph(undirected_matrix, False)

    powers = get_vertex_power(undirected_matrix, False)
    print('\nVertex powers:')
    for i in range(len(powers)):
        print(f'VERTEX {i + 1} power = {powers[i]}')

    print_homo_iso_hang_vertex(powers)
    turtle.exitonclick()


if __name__ == '__main__':
    main()
