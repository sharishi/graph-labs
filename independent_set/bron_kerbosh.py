from itertools import chain

adjacency_matrix = []
compsub = []

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

def bron_kerbosch(adjacency_matrix):

    results = []
    result = []

    def check(candidates, tested):
        for i in tested:
            q = True
            for j in candidates:
                if adjacency_matrix[i][j]:
                    q = False
                    break
            if q: return False
        return True

    def extend(compsub, candidates, tested):

        while candidates and check(candidates, tested):
            v = candidates[0]
            compsub.append(v)

            new_candidates = [ i for i in candidates if not adjacency_matrix[i][v] and i != v ]
            new_tested = [ i for i in tested if not adjacency_matrix[i][v]]

            if not new_candidates and not new_tested:
                result.append(list(compsub))
                results.clear()
                results.extend(list(compsub))

            else:
                extend(compsub, new_candidates, new_tested)

            candidates.remove(v)
            compsub.remove(v)
            tested.append(v)

    extend([], list(range(len(adjacency_matrix))), [])

    print("The list of  independent multiples ")
    for every_result in result:
        print([x + 1 for x in every_result])
    return results

# adjacency_matrix = [[0,1,1,0,1,0],
#                     [0,1,0,0,1,0],
#                     [0,0,0,0,0,0],
#                     [0,0,1,0,0,0],
#                     [0,0,0,1,0,0],
#                     [1,0,0,0,1,1], ]
# # Вызовите функцию bron_kerbosch с этой матрицей
# max_independent_set = bron_kerbosch(adjacency_matrix)
# print("Maximal Independent Set2:", [x + 1 for x in max_independent_set])


