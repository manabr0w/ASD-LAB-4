import turtle

from graph import draw_graph
from matrix_utils import (print_matrix, create_directed_matrix, get_reachability_matrix,
                          get_strong_connectivity_matrix, get_strong_connectivity_components)
from constants import SEED, NUM_VERTICES, K_MOD


def get_condensation_matrix(adjacency_matrix, strong_connectivity_components):
    num_vertices = len(adjacency_matrix)
    num_components = len(strong_connectivity_components)
    condensation_matrix = [[0] * num_components for _ in range(num_components)]

    for i in range(num_vertices):
        for j in range(num_vertices):
            if adjacency_matrix[i][j]:
                component_index_i = None
                component_index_j = None

                for index, component in enumerate(strong_connectivity_components):
                    if i + 1 in component:
                        component_index_i = index
                    if j + 1 in component:
                        component_index_j = index
                    if component_index_i is not None and component_index_j is not None:
                        break

                if component_index_i is not None and component_index_j is not None and component_index_i != component_index_j:
                    condensation_matrix[component_index_i][component_index_j] = 1

    return condensation_matrix


def main():
    modified_matrix = create_directed_matrix(SEED, NUM_VERTICES, K_MOD)

    reachability_matrix = get_reachability_matrix(modified_matrix)
    strong_connectivity_matrix = get_strong_connectivity_matrix(reachability_matrix)
    strong_connectivity_components = get_strong_connectivity_components(strong_connectivity_matrix)
    condensation_matrix = get_condensation_matrix(modified_matrix, strong_connectivity_components)

    print('Condensation matrix:')
    print_matrix(condensation_matrix)

    draw_graph(condensation_matrix, True)
    turtle.exitonclick()


if __name__ == '__main__':
    main()
