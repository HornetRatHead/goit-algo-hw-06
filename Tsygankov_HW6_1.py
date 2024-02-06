# Tsygankov_HW6_1

import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

# Додавання вершин
G.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

# Додавання ребер
G.add_edges_from([(1, 2), (1, 3), (1, 4), (2, 5), (2, 6), (3, 7), (7, 8), (4, 9), (4, 10), (4, 11), (10, 12), (10, 13), (13, 14), (14, 15), (14, 16), (16, 17), (16, 18), (17,19), (18, 20)])

# Візуалізація графа
nx.draw(G, with_labels=True, node_color='lightblue', node_size=1000, font_size=12, font_weight='bold')
plt.title("М-мережа")
plt.show()

# Аналіз характеристик графа
# Кількість вершин
num_nodes = G.number_of_nodes()
print("Кількість вершин у графі:", num_nodes)

# Кількість ребер
num_edges = G.number_of_edges()
print("Кількість ребер у графі:", num_edges)

# Ступінь вершин
degrees = dict(G.degree())
print("Ступінь кожної вершини:", degrees)