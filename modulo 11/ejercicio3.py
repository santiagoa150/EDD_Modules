from collections import deque


class Node:
    def __init__(self):
        self.visited = False


for _ in range(int(input())):
    people_exists = set()
    people = dict()
    families = dict()
    for _ in range(int(input())):
        new1, new2 = tuple(map(int, input().split()))
        if new1 in people_exists:
            families[new1].add(new2)
        else:
            people_exists.add(new1)
            people[new1] = Node()
            families[new1] = {new2}

        if new2 in people_exists:
            families[new2].add(new1)
        else:
            people_exists.add(new2)
            people[new2] = Node()
            families[new2] = {new1}

    total_families = 0
    bigger_family = 0
    for person in people_exists:
        if not people[person].visited:
            total_families += 1
            people[person].visited = True
            q = deque()
            q.append(person)
            total_current_family = 1
            while q:
                a = q.popleft()
                for b in families[a]:
                    if not people[b].visited:
                        people[b].visited = True
                        total_current_family += 1
                        q.append(b)
            if total_current_family > bigger_family:
                bigger_family = total_current_family
    print(total_families, bigger_family)
