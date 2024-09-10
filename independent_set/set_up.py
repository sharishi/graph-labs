import tkinter as tk
from tkinter import messagebox
import turtle
from bron_kerbosh import generate_matrix, matrix_filling, bron_kerbosch
import math

# Global variables
nodes_count = 0
ribs_data = []
adjacency_matrix = []
visited = []
max_independent_set = []
start_point = 0
t = None  # Initialize the global variable t
dict_list = None
current_vertex = 0
# max_independent_set = []


def reset_program():
    global nodes_count, ribs_data, adjacency_matrix, visited, max_independent_set, start_point, t, canvas

    # Сброс всех переменных
    nodes_count = 0
    ribs_data = []
    adjacency_matrix = []
    visited = []
    max_independent_set = []
    start_point = 0

    # Включение полей ввода
    vertices_entry.config(state=tk.NORMAL)
    start_entry.config(state=tk.NORMAL)

    # Очистка полей ввода
    vertices_entry.delete(0, tk.END)
    ribs_entry.delete(0, tk.END)
    start_entry.delete(0, tk.END)

    # Закрытие окна с визуализацией, если оно было открыто
    try:
        turtle.bye()
    except turtle.Terminator:
        pass

    root.update()  # Обновить главное окно Tkinter

    # Очистка canvas в Tkinter
    canvas.delete("all")  # Удалить все объекты на canvas
    canvas.config(scrollregion=canvas.bbox("all"))  # Сбросить размеры canvas
    canvas.update_idletasks()  # Применить изменения размеров canvas

    # Инициализация черепахи
    t = None


def on_vertices_button_click():
    global nodes_count
    nodes_text = vertices_entry.get()
    try:
        nodes_count = int(nodes_text)
        vertices_entry.config(state=tk.DISABLED)  # Disable the vertices entry after input
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer for the number of vertices")


def on_ribs_button_click():
    counter = 0
    ribs_text = ribs_entry.get()
    try:
        a, b = map(int, ribs_text.split())
        # print(a, b)
        # print(nodes_count)
        if (a > nodes_count or a <= 0) or (b > nodes_count or b <= 0):
            messagebox.showerror("Error", "Please enter valid vertex numbers")
        elif (a, b) in ribs_data or (b, a) in ribs_data or a == b:
            messagebox.showerror("Error", "Such a rib already exists")
        elif counter == int(nodes_count*(nodes_count - 1)/2):
            messagebox.showerror("Error", "You can't build any more ribs")
        else:
            ribs_data.append((a, b))
            counter += 1
            ribs_entry.delete(0, tk.END)  # Clear the entry after input
    except ValueError:
        messagebox.showerror("Error", "Please enter two valid integers separated by a space")


def start_button_click():
    global start_point
    start_point = start_entry.get()
    if int(start_point) <= nodes_count:
        try:
            start_entry.config(state=tk.DISABLED)  # Disable the vertices entry after input
            start_point = int(start_point)  # Попытка преобразования в целое число

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer for the number of vertices")
    else:
        messagebox.showerror("Error", "Such a vertex does not exist")


def display_data():
    # Создание окна для отображения данных
    data_window = tk.Toplevel()
    data_window.title("Matrix and Sequence Viewer")

    # Создание и размещение виджетов Label для отображения данных
    matrix_label = tk.Label(
        data_window,
        text="Matrix Data:\n" + "\n".join([" ".join(map(str, row)) for row in adjacency_matrix])
    )

    matrix_label.pack()

    sequence_label = tk.Label(data_window, text="Sequence Data: " + " ".join(map(str, [x + 1 for x in max_independent_set])))
    sequence_label.pack()


def quit_program():
    result = messagebox.askyesno("Quit", "Do you want to quit the program?")
    if result:
        turtle.bye()
        root.quit()


# Создаю основное Tkinter окно
root = tk.Tk()
root.title("Graph Input and Visualization")

# Создаю холст для черепашки
canvas = turtle.ScrolledCanvas(root)
canvas.pack()
canvas.grid(row=0, column=0, rowspan=9, sticky="nsew")

# Создаю и настраиваю сетки для правой части окна
right_frame = tk.Frame(root)
right_frame.grid(row=0, column=1, sticky="n")


def visualize_graph_traversal():
    if nodes_count == 0 or not ribs_data:
        messagebox.showwarning("Warning", "Please enter the number of vertices and at least one edge.")
        return

    global t, dict_list    # Глобальная переменная, чтобы отслеживать текущую вершину в обходе
    global current_vertex
    # Сделаем t глобальной переменной, чтобы его можно было закрыть при сбросе

    t = turtle.RawTurtle(canvas)
    t.shape("turtle")
    t.color('#782850')
    t.pensize(3)

    # Расстояние между вершинами
    vertex_distance = 100

    # Максимальное количество вершин в ряду
    max_vertices_per_row = 2

    window_width = max(800, len(adjacency_matrix) * vertex_distance)
    window_height = max(600, len(adjacency_matrix) * vertex_distance)

    # Устанавливаем размер окна Tkinter
    root.geometry(f"{window_width}x{window_height}")

    # Показываем окно
    root.deiconify()

    # Строю матрицу смежности
    f_matrix = generate_matrix(nodes_count)
    adjacency_matrix.extend(matrix_filling(f_matrix, ribs_data))
    # print("adjm",adjacency_matrix)

    # Initialize the visited list
    # global visited
    # visited = [False] * nodes_count

    # Start DFS traversal from the first vertex (vertex 1)
    global  max_independent_set
    max_independent_set = bron_kerbosch(adjacency_matrix)
    print("Maximal Independent Set:", [x + 1 for x in max_independent_set])

    def draw_vertices(num_vertices, dict_value=None):
        if dict_value is None:
            dict_value = dict()

        # Радиус окружности
        radius = 150
        # Угол между вершинами (в радианах)
        angle = (2 * math.pi) / num_vertices

        for enum, i in enumerate(range(num_vertices)):
            x = radius * math.cos(i * angle)
            y = radius * math.sin(i * angle)
            dict_value[enum + 1] = [x, y]

            t.penup()
            t.goto(x, y)
            t.pendown()
            t.circle(20)  # Рисуем вершину как круг (или другую фигуру)

            t.penup()
            t.goto(x, y + 13)  # Adjust position for value text
            t.pendown()
            t.write(str(enum + 1), align="center", font=("Arial", 12, "normal"))

        return dict_value


    # Функция для рисования ребер графа
    def draw_edges(adjacency__matrix, dict_value):
        num_vertices = len(adjacency__matrix)
        radius = 150

        for i in range(1, num_vertices + 1):
            x1, y1 = dict_value[i]
            t.penup()
            t.goto(x1, y1)
            t.pendown()

            for j in range(i + 1, num_vertices + 1):
                if adjacency_matrix[i - 1][j - 1] == 1:
                    x2, y2 = dict_value[j]
                    t.penup()
                    t.goto(x1, y1)
                    t.pendown()
                    t.goto(x2, y2)
                    t.penup()

        t.penup()

    # Функция для перехода к следующей вершине в обходе
    def move_to_next_vertex():
        global current_vertex

        if current_vertex < len(max_independent_set):
            vertex_number = max_independent_set[current_vertex]  # Получаем номер следующей вершины
            if vertex_number in dict_links:
                x, y = dict_links[vertex_number + 1]  # Получаем координаты вершины из словаря
                t.penup()
                t.goto(x, y)
                t.color('#7da8d4')
                t.pendown()
                t.dot(25)  # Рисуем маркер в текущей вершине
                current_vertex += 1
            else:
                messagebox.showwarning("Warning", f"Vertex {vertex_number} is missing coordinates.")
        else:
            messagebox.showinfo("Info", "Traversal is complete.")
            return  # Завершаем выполнение функции, если обход завершен
        root.after(1000, move_to_next_vertex)  # Вызываем функцию через 1000 миллисекунд (1 секунда)

    # Вызываем функции для рисования вершин и ребер графа
    dict_links = draw_vertices(len(adjacency_matrix))
    draw_edges(adjacency_matrix, dict_links)
    move_to_next_vertex()


# Create and place labels and entry widgets
vertices_label = tk.Label(right_frame, text="Enter the number of vertices:")
vertices_label.grid(row=0, column=0, columnspan=2)

vertices_entry = tk.Entry(right_frame)
vertices_entry.grid(row=0, column=2, columnspan=2)

ribs_label = tk.Label(right_frame, text="Enter edges as pairs (e.g., '1 2', '2 3'):")
ribs_label.grid(row=1, column=0, columnspan=2)

ribs_entry = tk.Entry(right_frame)
ribs_entry.grid(row=1, column=2, columnspan=2)

start_label = tk.Label(right_frame, text="Enter the start point, please:")
start_label.grid(row=2, column=0, columnspan=2)

start_entry = tk.Entry(right_frame)
start_entry.grid(row=2, column=2, columnspan=2)

# Create and place buttons
vertices_button = tk.Button(right_frame, text="Add tops", command=on_vertices_button_click, width=17, pady=7)
vertices_button.grid(row=3, column=0)

ribs_button = tk.Button(right_frame, text="Add Edge", command=on_ribs_button_click, width=17, pady=7)
ribs_button.grid(row=3, column=1)

start_button = tk.Button(right_frame, text="Add start point", command=start_button_click, width=17, pady=7)
start_button.grid(row=3, column=2, columnspan=2)

visualize_button = tk.Button(right_frame, text="Visualize Graph Traversal", command=visualize_graph_traversal,
                             width=30, pady=10)
visualize_button.grid(row=4, column=0, columnspan=4)

info_button = tk.Button(right_frame, text="Show Info", command=display_data, width=30, pady=10)
info_button.grid(row=5, column=0, columnspan=4)

reset_button = tk.Button(right_frame, text="Reset Program", command=reset_program, width=30, pady=10)
reset_button.grid(row=6, column=0, columnspan=4)

quit_button = tk.Button(right_frame, text="Quit", command=quit_program, width=30, pady=15)
quit_button.grid(row=7, column=0, columnspan=4)

# Configure row and column weights for resizing
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)


root.mainloop()

