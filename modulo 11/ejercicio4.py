from collections import deque


class Node:
    def __init__(self):
        self.visited = False
        self.color = None


other = {
    'R': 'B',
    'B': 'R'
}


def is_bipartite(nodes_p, edges, all_names) -> bool:
    for start in all_names:
        if not nodes_p[start].visited:
            nodes_p[start].visited = True
            nodes_p[start].color = 'R'
            q = deque()
            q.append(start)

            while q:
                a = q.popleft()
                for b in edges[a]:
                    if not nodes_p[b].visited:
                        nodes_p[b].visited = True
                        q.append(b)
                        nodes_p[b].color = other[nodes_p[a].color]
                    else:
                        if nodes_p[b].color == nodes_p[a].color:
                            return False
    return True


for _ in range(int(input())):
    total_nodes, total_lines = tuple(map(int, input().split()))
    node_names = set()
    all_nodes = dict()
    lines = dict()
    for _ in range(total_lines):
        from_node, to_node = tuple(map(int, input().split(', ')))
        if from_node in node_names:
            lines[from_node].add(to_node)
        else:
            node_names.add(from_node)
            all_nodes[from_node] = Node()
            lines[from_node] = {to_node}

        if to_node in node_names:
            lines[to_node].add(from_node)
        else:
            node_names.add(to_node)
            all_nodes[to_node] = Node()
            lines[to_node] = {from_node}

    try:
        if is_bipartite(all_nodes, lines, node_names):
            print('bipartito')
        else:
            print('no bipartito')
    except:
        print('bipartito')
