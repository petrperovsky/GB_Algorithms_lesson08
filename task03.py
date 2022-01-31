"""Написать программу, которая обходит не взвешенный ориентированный граф без петель,
в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
Примечания:
a. граф должен храниться в виде списка смежности;
b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин."""
import random

n = int(input('Введите количество вершин: '))
s = int(input('С какой вершины начать обход: '))


def create_graf(vertex):
    '''Создание ориентированного невзвешенного графа с заданным количеством вершин'''

    graph = {}
    for i in range(vertex):
        graph[i] = set()
        for j in range(vertex // 2):
            edge = random.randint(0, vertex)
            if edge != i:
                graph[i].add(edge)
    return graph

g = create_graf(n)
print('Граф:')
for key, value in g.items():
    print('\t', key, ':', value)


def dfs(graph, vertex, visited=None, way=None):
    if visited is None:
        visited = set()
    if way is None:
        way = []
    visited.add(vertex)
    way.append(vertex)
    for next in graph[vertex]:
        if next not in visited:
            dfs(graph, next, visited, way)
    return visited, way


v, w = dfs(g, s)

print(f'Путь обхода из точки {s}:\n\t{w}')

'''Честно, сломал голову, что не работает
'''

