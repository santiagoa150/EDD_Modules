from collections import deque


class Node:
    def __init__(self):
        self.visited = False
        self.level = -1


def bfs(nodes, edges, start, levels):
    nodes[start].visited = True
    q = deque()
    q.append(start)
    while q:
        a = q.popleft()
        for b in edges[a]:
            if not nodes[b].visited:
                nodes[b].visited = True
                current = nodes[a].level + 1
                nodes[b].level = current
                q.append(b)
                try:
                    levels[current] += 1
                except:
                    levels[current] = 1


people_count = int(input())
people = dict()
friends = dict()

for person in range(people_count):
    new_friends = list(map(int, input().split()))
    people[person] = Node()
    friends[person] = set([f for f in new_friends if f != -1])

for case in tuple(map(int, input().split(', '))):
    levels = {}
    people[case].level = 0
    bfs(people, friends, case, levels)
    default = (0, 0)
    for key, value in levels.items():
        if value > default[1]:
            default = (key, value)
    if default[0] == 0:
        print(0)
    else:
        print(default[0], default[1])
    for p in people:
        people[p].level = -1
        people[p].visited = False
