# Tsygankov_HW6_3

import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

# Додавання вершин
G.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

# Додавання ребер з вагами
edges_with_weights = [
    (1, 2, {'weight': 1}), (1, 3, {'weight': 2}), (1, 4, {'weight': 3}), 
    (2, 5, {'weight': 2}), (2, 6, {'weight': 1}), (3, 7, {'weight': 2}), 
    (7, 8, {'weight': 3}), (4, 9, {'weight': 2}), (4, 10, {'weight': 1}), 
    (4, 11, {'weight': 2}), (10, 12, {'weight': 3}), (10, 13, {'weight': 2}), 
    (13, 14, {'weight': 1}), (14, 15, {'weight': 2}), (14, 16, {'weight': 3}), 
    (16, 17, {'weight': 2}), (16, 18, {'weight': 1}), (17, 19, {'weight': 2}), 
    (18, 20, {'weight': 3})
]
G.add_edges_from(edges_with_weights)

# Візуалізація графа з вагами ребер
pos = nx.spring_layout(G)  # Задаємо позиції вершин для кращої візуалізації
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1000, font_size=12, font_weight='bold')

# Відображення ваг ребер
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.title("Мережа")
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

# Алгоритм Дейкстри
def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.keys())

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])
        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, attr in graph[current_vertex].items():
            distance = distances[current_vertex] + attr['weight']

            if distance < distances[neighbor]:
                distances[neighbor] = distance

        unvisited.remove(current_vertex)

    return distances

if __name__ == '__main__':
    # Пошук найкоротших відстаней від вершини 1
    start_node = 1
    distances_from_start = dijkstra(G.adj, start_node)
    print("Найкоротші відстані від вершини", start_node, "до всіх інших вершин:", distances_from_start)
