import turtle

from constants import SEED, NUM_VERTICES, K
from matrix_utils import (print_matrix, create_directed_matrix, get_vertex_power,
                          print_half_power_vertex, print_homo_iso_hang_vertex)
from graph import draw_graph


def main():
    directed_matrix = create_directed_matrix(SEED, NUM_VERTICES, K)
    print('Directed matrix:')
    print_matrix(directed_matrix)
    draw_graph(directed_matrix, True)

    powers = get_vertex_power(directed_matrix, True)
    print('\nVertex power:')
    for i in range(len(powers)):
        print(f'VERTEX {i + 1} power = {powers[i]}')

    print('\nVertex half power:')
    print_half_power_vertex(directed_matrix)

    print_homo_iso_hang_vertex(powers)

    turtle.exitonclick()


if __name__ == '__main__':
    main()
