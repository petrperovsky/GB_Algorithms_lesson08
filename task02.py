"""Доработать алгоритм Дейкстры (рассматривался на уроке),
чтобы он дополнительно возвращал список вершин, которые необходимо обойти."""

g = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 7, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0]
]


def dijkstra(graph, start):
    l = len(graph)
    is_visited = [False] * l
    cost = [float('inf')] * l
    parent = [-1] * l
    cost[start] = 0
    min_cost = 0

    while min_cost < float('inf'):
        is_visited[start] = True
        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:
                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start
        min_cost = float('inf')

        for i in range(l):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i

    way = [[] for _ in range(l)]
    for i in range(l):
        if is_visited[i]:
            way[i].append(i)
            j = i
            while parent[j] != -1:
                way[i].append(parent[j])
                j = parent[j]
            way[i].reverse()

    return cost, way

s = int(input('Введите точку старта от 0 до 7: '))
cost, way = dijkstra(g, s)
for i in range(len(g)):
    print(f'Из старта до точки {i} быстрее можно добраться путем '
          f'{way[i]}, и это займет {cost[i]} усл ед')


