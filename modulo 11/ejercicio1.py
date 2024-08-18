from collections import deque


class Node:
    def __init__(self):
        self.visited = False
        self.number = -1


def bfs(nodes, edges, start):
    nodes[start].visited = True
    q = deque()
    q.append(start)
    while q:
        a = q.popleft()
        for b in edges[a]:
            if not nodes[b].visited:
                nodes[b].visited = True
                nodes[b].number = nodes[a].number + 1
                q.append(b)


total = int(input())
for i in range(1, total + 1):
    inv, total_dances = tuple(map(int, input().split(', ')))
    dances = dict()
    nodes_param = dict()
    for j in range(inv):
        dances[j] = set()
        nodes_param[j] = Node()
    nodes_param[0].number = 0
    for _ in range(total_dances):
        from_dance, to_dance = tuple(map(int, input().split()))
        dances[from_dance].add(to_dance)
        dances[to_dance].add(from_dance)
    bfs(nodes_param, dances, 0)

    print(f'fiesta {i}:')
    for k in range(1, inv):
        if nodes_param[k].number < 0:
            print(k, 'INF')
        else:
            print(k, nodes_param[k].number)
    if i < total:
        print()
