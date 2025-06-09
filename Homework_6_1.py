import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

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

# ----------------------------------------
# Короткий аналіз графу
# ----------------------------------------

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

# ----------------------------------------
# DFS шлях
# ----------------------------------------

def dfs_search(graph, start_vertex, target, visited=None, path=None):
  if visited is None:
    visited = set()
  if path is None:
     path = []

  visited.add(start_vertex)
  path.append(start_vertex)

  if start_vertex == target:
     return path

  for neighbor in graph[start_vertex]:
    if neighbor not in visited:
      result = dfs_search(graph, neighbor, target, visited, path.copy())
      if result:
         return result
  return None


# ----------------------------------------
# BFS шлях
# ----------------------------------------

def bfs_search(graph, start_vertex, target, visited=None):
  if visited is None:
    visited = set()
  queue = deque([[start_vertex]])
  
  
  while queue:
    path = queue.popleft()
    node = path[-1]
    if node == target:
      return path
    
    if node not in visited:
      visited.add(node)
      for neighbor in graph[node]:
        new_path = list(path) 
        new_path.append(neighbor)
        queue.append(new_path)
  return None

# ----------------------------------------
# Вивід найкоротших маршрутів з початковою та кінцевою точкою
# ----------------------------------------


dfs_path = dfs_search(graph, start, end)
bfs_path = bfs_search(graph, start, end)

print(f"\nЯкщо розраховувати маршрут за DFS наприклад від {start} до {end}, то отримаємо наступний результат: {dfs_path}.")
print(f"\nЯкщо розраховувати маршрут за BFS наприклад від {start} до {end}, то отримаємо наступний результат: {bfs_path}.\n")


print("===" * 25)
print(f"\nА зараз розрахуємо найкоротший маршрут від {start} та до усіх інших населених пунктів за рахунок алгоритму Дейкстри.")


# ----------------------------------------
# Побудова алгоритму Дейкстри
# ----------------------------------------

# Я не залучала таблицю виводу для кожного кроку, оскільки здійснила 
# власний вивід відповідно до бази даних та задачі розрахунку найкоротшого 
# шляху, а не лише підрахунок загалом кілометрів
def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.keys())
    visited = []
    previous = {vertex: None for vertex in graph}

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_vertex

        visited.append(current_vertex)
        unvisited.remove(current_vertex)

    return distances, previous



# ----------------------------------------
# Вивід результатів з підрахунком найкоротших шляхів від початкової точки 
# до усіх інших населених пунктів
# ----------------------------------------


def reconstruct_path(previous, start, target):
    path = []
    current = target
    while current:
        path.insert(0, current)
        current = previous[current]
    return path if path[0] == start else None


distances, previous = dijkstra(graph, start)
for city in graph:
    if city != start:
        path = reconstruct_path(previous, start, city)
        print(f"{start} -> {city}: шлях = {path}, довжина = {distances[city]} км")
