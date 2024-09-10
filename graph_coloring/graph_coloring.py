def generate_matrix(top_count):
    matrix = [[0 for _ in range(top_count)] for _ in range(top_count)]
    return matrix


def matrix_filling(source_matrix, list_of_ribs):
    print(list_of_ribs)
    for couple in list_of_ribs:
        source_matrix[couple[0] - 1][couple[1] - 1] = source_matrix[couple[1] - 1][couple[0] - 1] = 1
    return source_matrix


def sort_vertices_by_degree(matrix):
    num_vertices = len(matrix)
    degrees = [sum(row) for row in matrix]

    # Создаю список кортежей, где первый элемент - вершина, а второй - её степень
    vertices_with_degrees = list(zip(range(num_vertices), degrees))

    # Сортирую по убыванию степени
    sorted_vertices = [vertex for vertex, _ in sorted(vertices_with_degrees, key=lambda x: x[1], reverse=True)]

    print(sorted_vertices)

    return sorted_vertices


def item_remove(main_list, interim_list):
    for item in interim_list:
        if item in main_list:
            main_list.remove(item)

    interim_list.clear()


def color_graph(adjacency_matrix):

    sorted_vertices = sort_vertices_by_degree(adjacency_matrix)
    copy_sort = sorted_vertices.copy()
    print(sorted_vertices)

    current_color = 0
    colors = {}  # Словарь для хранения цветов вершин

    while copy_sort:
        colors[current_color] = []
        temporary_list = list()

        colors[current_color].append(copy_sort[0])
        copy_sort.remove(copy_sort[0])

        for other_vertex in copy_sort:
            if all(adjacency_matrix[other_vertex][neighbour] == 0 for neighbour in colors[current_color]):
                colors[current_color].append(other_vertex)
                temporary_list.append(other_vertex)

        item_remove(copy_sort, temporary_list)

        print("copy_sort", copy_sort)

        current_color += 1

    return colors


adjacency_m = [[0, 1, 1, 0, 1, 1],
               [1, 0, 0, 0, 1, 0],
               [1, 0, 0, 1, 0, 0],
               [0, 0, 1, 0, 1, 0],
               [1, 1, 0, 1, 0, 1],
               [1, 0, 0, 0, 1, 0]]
result = color_graph(adjacency_m)
print(result)


# def print_array(array):
#     print("###")
#     print(array)
#     print("###")
#
#
# def math_task(data):
#     answer = []
#     # возводим в третью степень
#     for elem in data:
#         answer += [elem ** 3]
#
#     print_array(answer)
#
#     # берем остаток от деления на 7
#     for i in range(len(answer)):
#         answer[i] = answer[i] % 7
#
#     print_array(answer)
#
#     # прибавляем к остатку изначальный массив
#     for i in range(len(answer)):
#         answer[i] = answer[i] + data[i]
#
#     print_array(answer)
#
#     # возвращаем результат
#     return answer

# def sum_as_ints(string_list):
#     summ = 0
#     for string in string_list:
#         try:
#             summ += int(string)
#         except ValueError:
#             print("invalid literal for int()")
#             pass
#
#     return summ
#
#
# summary = sum_as_ints(['1','2,2','3dcc','4'])
# print(summary)

# def find_substr(substring, string):
#     start = string.find(substring)
#     if start != -1:
#         end = start + len(substring)
#         return (start, end)
#     else:
#         return None

# def fifth_element(list_s):
#     return list_s[-5::-5]

# def process_string(string):
#     result = string[1:].lower()
#     result = result.replace('intern', 'junior')
#     return result

'''В этом задании необходимо написать функцию check_string, которая сначала проверяет строку
 на наличие лишних символов пробела слева и справа. Если есть лишние пробелы, то тогда мы считаем
  строку неверной. Затем проверяет, что только первое слово начинается с большой буквы, а остальные
   с маленькой, и в конце проводит проверку, что последний символ является точкой.'''

#
# def check_string(string):
#     result = True
#     splitted_string = string.split()
#     if string.strip() != string:
#         result = False
#     if string[-1] != '.':
#         result = False
#     if splitted_string[0][0].islower():
#         result = False
#     for split in splitted_string[1:]:
#         if split[0].isupper():
#             result = False
#
#     return result

