import random
import math
adjacency_matrix = []
compsub = []

def generate_matrix(top_count):
    matrix = [[0 for _ in range(top_count)] for _ in range(top_count)]
    # print(f'matrix with dimension {top_count} x {top_count} is {matrix}')
    return matrix


def matrix_filling(source_matrix, list_of_ribs):
    print(list_of_ribs)
    for couple in list_of_ribs:
        # print(couple)
        source_matrix[couple[0] - 1][couple[1] - 1] = source_matrix[couple[1] - 1][couple[0] - 1] = 1
    return source_matrix


adjacency_matrix = [[0,1,1,0,1,0],
                    [0,1,0,0,1,0],
                    [0,0,0,0,0,0],
                    [0,0,1,0,0,0],
                    [0,0,0,1,0,0],
                    [1,0,0,0,1,1],]

