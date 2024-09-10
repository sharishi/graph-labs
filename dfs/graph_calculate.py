def generate_matrix(top_count):
    matrix = [[0 for _ in range(top_count)] for _ in range(top_count)]
    print(f'matrix with dimension {top_count} x {top_count} is {matrix}')
    return matrix


def matrix_filling(source_matrix, list_of_ribs):
    for couple in list_of_ribs:
        print(couple)
        source_matrix[couple[0] - 1][couple[1] - 1] = source_matrix[couple[1] - 1][couple[0] - 1] = 1
        for row_1 in source_matrix:
            print(row_1)
    return source_matrix


def dfs_by_matrix(graph, start, visited_tops, list_value=None):
    if list_value is None:
        list_value = []  # Create a new empty list
    print("Visited:", start)
    list_value.append(start)
    visited_tops[start - 1] = True

    for i, values in enumerate(graph[start - 1]):
        if values == 1 and not visited_tops[i]:
            dfs_by_matrix(graph, i + 1, visited_tops, list_value)

    return list_value





