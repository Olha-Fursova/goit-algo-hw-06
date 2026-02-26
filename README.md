## Analysis of transport network graphs of Zhytomyr region
# Task 1 — Graph construction
A transport network graph of the region with 6 settlements was created: Berdychiv, Zhytomyr, Andrushivka, Korostyshiv, Radomyshl and Malyn.

The networkx library was used to construct the graph.

Edge weights reflect the real distances between points (in km, according to car routes).

The graph was visualized using networkx and matplotlib.

# Main characteristics:

Number of vertices: 6

Number of edges: 9

Degrees of vertices:

Berdychiv: 2

Zhytomyr: 4

Andrushivka: 3

Korostyshiv: 3

Radomyshl: 2

Malyn: 2

# Task 2 — Path search (DFS and BFS)
DFS algorithm (depth): built in the form of the dfs_search method. A route deep into the graph from a given vertex (Berdychiv) is built. Since the DFS algorithm moves mostly into the depth of the graph branch, and does not find the shortest path, the output showed us a longer path.

BFS algorithm (breadth): implemented in the form of the bfs_search method. The shortest path in the number of transitions is built. According to the results, you can see that this algorithm chose the shortest path and with the fewest detour points. As a result, the total selected mileage turned out to be less than in the DFS calculations

# Example:
DFS from Berdychiv: ['Berdychiv', 'Zhytomyr', 'Korostyshiv', 'Radomyshl', 'Malyn']

BFS from Berdychiv to Malyn: ['Berdychiv', 'Zhytomyr', 'Malyn']

DFS first moves in depth, not guaranteeing the shortest path.

BFS searches the path in breadth, therefore finds the minimum number of transitions between nodes.

# Task 3 — Dijkstra's Algorithm
Dijkstra's algorithm is implemented to find the shortest paths from Berdychiv to all other points, taking into account real weights (distances).

# Example of the result:
Berdychiv -> Zhytomyr: path = ['Berdychiv', 'Zhytomyr'], length = 41 km.

Berdychiv -> Korostyshiv: path = ['Berdychiv', 'Zhytomyr', 'Korostyshiv'], length = 75 km.

Berdychiv -> Radomyshl: path = ['Berdychiv', 'Zhytomyr', 'Korostyshiv', 'Radomyshl'], length = 116 km.

Berdychiv -> Malyn: path = ['Berdychiv', 'Zhytomyr', 'Malyn'], length = 128 km.

Berdychiv -> Andrushivka: path = ['Berdychiv', 'Andrushivka'], length = 46 km.

## Conclusions
BFS is suitable for finding the shortest path in terms of the number of steps.

DFS is for a complete traversal or depth-of-field study of the graph structure.

Dijkstra's algorithm is ideal for quickly finding the shortest path by weight between points, which is illustrated by the results. Of course, this is still far from a real navigation build, but the results coincided with those indicated as "fastest" in Google Maps.

The constructed graph clearly models a transport network with (almost) real parameters. I left only integers in the specified weights in kilometers, without decimals.





## Аналіз графів транспортної мережі Житомирщини
 # Завдання 1 — Побудова графа
 Створено граф транспортної мережі регіону з 6 населеними пунктами: Бердичів, Житомир, Андрушівка, Коростишів, Радомишль та Малин.

 Для побудови графа використано бібліотеку networkx.

 Ваги ребер відображають реальні відстані між пунктами (у км, згідно маршрутів автомобілем).

 Граф візуалізовано з допомогою networkx та matplotlib.

 # Основні характеристики:

 Кількість вершин: 6 
 
 Кількість ребер: 9 


 Ступені вершин: 
 
 Бердичів: 2 
 
 Житомир: 4 
 
 Андрушівка: 3 

 Коростишів: 3 
 
 Радомишль: 2 
 
 Малин: 2 

 # Завдання 2 — Пошук шляхів (DFS та BFS)
 Алгоритм DFS (глибина): побудовано у вигляді методу dfs_search. Побудовано маршрут вглиб графа від заданої вершини (Бердичів). Оскільки алгоритм DFS рухається здебільшого в глибину гілки графу, а не знайходить найкоротший шлях, вивід показав нам довший шлях. 

 Алгоритм BFS (ширина): реалізовано у вигляді методу bfs_search. Побудовано найкоротший шлях у кількості переходів. За результатами можна побачити, що даний алгоритм вибрав найкоротший шлях та з найменшою кількістю обхідних точок. У результаті загальний обраний кілометраж виявився меншим, ніж у підрахунках DFS 

 # Приклад:
 DFS від Бердичева: ['Бердичів', 'Житомир', 'Коростишів', 'Радомишль', 'Малин']

 BFS від Бердичева до Малина: ['Бердичів', 'Житомир', 'Малин']

 DFS спершу рухається вглиб, не гарантуючи найкоротший шлях.

 BFS шукає шлях у ширину, тому знаходить мінімальну кількість переходів між вузлами.

 # Завдання 3 — Алгоритм Дейкстри
 Реалізовано алгоритм Дейкстри для знаходження найкоротших шляхів від Бердичева до усіх інших пунктів з урахуванням реальних ваг (відстаней).


 # Приклад результату:
 Бердичів -> Житомир: шлях = ['Бердичів', 'Житомир'], довжина = 41 км. 
 
 Бердичів -> Коростишів: шлях = ['Бердичів', 'Житомир', 'Коростишів'], довжина = 75 км. 
 
 Бердичів -> Радомишль: шлях = ['Бердичів', 'Житомир', 'Коростишів', 'Радомишль'], довжина = 116 км. 
 
 Бердичів -> Малин: шлях = ['Бердичів', 'Житомир', 'Малин'], довжина = 128 км. 
 
 Бердичів -> Андрушівка: шлях = ['Бердичів', 'Андрушівка'], довжина = 46 км. 
 

## Висновки
 BFS підходить для знаходження найкоротшого у кількості кроків маршруту.

 DFS — для повного обходу або дослідження глибини структури графа.

 Алгоритм Дейкстри ідеально підходить для швидкого знаходження найкоротшого шляху за вагою між точками, що ілюструється результатами. Звісно, це ще далеко від реальної побудови навігації, але результати збігалися з тими, що були вказані як "найшвидші" у Google Map.

 Побудований граф наочно моделює транспортну мережу з (майже) реальними параметрами. Я залишила лише цілі числа у визначені ваги у кілометрах, без чисел після коми.

