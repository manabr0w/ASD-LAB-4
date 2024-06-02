import turtle

from constants import SEED, K_MOD, NUM_VERTICES
from matrix_utils import (print_matrix, create_directed_matrix, print_half_power_vertex,
                          print_paths_of_vertexes, get_reachability_matrix,
                          get_strong_connectivity_matrix, get_strong_connectivity_components)
from graph import draw_graph


def main():
    modified_matrix = create_directed_matrix(SEED, NUM_VERTICES, K_MOD)
    print('Modified matrix:')
    print_matrix(modified_matrix)
    draw_graph(modified_matrix, True)

    print('\nVertex half power:')
    print_half_power_vertex(modified_matrix)

    print_paths_of_vertexes(modified_matrix)

    reachability_matrix = get_reachability_matrix(modified_matrix)
    print('\nReachability matrix:')
    print_matrix(reachability_matrix)

    strong_connectivity_matrix = get_strong_connectivity_matrix(reachability_matrix)
    print('\nStrong connectivity matrix:')
    print_matrix(strong_connectivity_matrix)

    strong_connectivity_components = get_strong_connectivity_components(strong_connectivity_matrix)

    for i in range(len(strong_connectivity_components)):
        print(f'\nCOMPONENT {i + 1}: {strong_connectivity_components[i]}')

    turtle.exitonclick()


if __name__ == '__main__':
    main()
