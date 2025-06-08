import networkx as nx
import matplotlib.pyplot as plt

# Моє рідне місто - Бездичів, тож за основу/початок графа візьму саме 
# його. Залучу до гарфу також деякі міста та села Житомирщини та 
# надам їм вагу у кількості кілометрів між ними (враховуючи маршрути автівкою)
graph = {
    'Бердичів': {'Житомир': 41, 'Андрушівка': 46},
    'Житомир': {'Бердичів': 41, 'Коростишів': 34, 'Малин': 87, 'Андрушівка': 45},
    'Коростишів': {'Житомир': 34, 'Радомишль': 41, 'Андрушівка': 69},
    'Радомишль': {'Коростишів': 41, 'Малин': 35},
    'Малин': {'Житомир': 87, 'Радомишль': 35},
    'Андрушівка': {'Бердичів': 46, 'Житомир': 45, 'Коростишів': 69}
}

G = nx.Graph()

# Явно додаємо ребра з вагою
for city, neighbors in graph.items():
    for neighbor, distance in neighbors.items():
        G.add_edge(city, neighbor, weight=distance)

pos = nx.spring_layout(G)
options = {
  "node_size": 4500,
  "font_size": 10,
  "font_color": "white",
  "node_color": "green",
  "edge_color": "gray",
  "with_labels": True,
  "width": 3,
  "arrows": True
}


nx.draw(G, pos, **options)
plt.title("Транспортна мережа Житомирщини")
plt.show()

num_of_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()

print(f"\nДо графіку залучено {num_of_nodes} міст та сіл разом.")
print(f"\nЗагальна кількість можливих пересувань між містами та селами (з'єднання дорогами): {num_edges}.")
print("\nСтупенями кожного населеного пункту є:")
for node, degree in G.degree():
  print(f"{node}: {degree}")

print("===" * 25)

start = "Бердичів"
end = "Малин"

# DFS шлях
dfs_path_list = list(nx.dfs_edges(G, source=start))
dfs_nodes = [start]
for u, v in dfs_path_list:
  if v not in dfs_nodes:
    dfs_nodes.append(v)

# BFS шлях

bfs_tree_obj = nx.bfs_tree(G, start)
bfs_path = nx.shortest_path(bfs_tree_obj, source=start, target=end)

print(f"\nЯкщо розраховувати маршрут за DFS від {start} і далі у глибину гілки з дорогами до інших населених пунктів, то отримаємо наступний результат: {dfs_nodes}.")
print(f"\nЯкщо розраховувати маршрут за BFS наприклад від {start} до {end}, то отримаємо наступний результат: {bfs_path}.")


print("===" * 25)
print(f"\nА зараз розрахуємо найкоротший маршрут від {start} та до усіх інших населених пунктів за рахунок алгоритму Дейкстри.")

for target in G.nodes():
  if target != start:
    try:
      path = nx.dijkstra_path(G, source=start, target=target, weight="weight")
      distance = nx.dijkstra_path_length(G, source=start, target=target, weight='weight')
      print(f"{start} -> {target}: шлях = {path}, довжина = {distance} км.")
    except nx.NetworkXNoPath:
      print(f"{start} -> {target}: шляху немає.")