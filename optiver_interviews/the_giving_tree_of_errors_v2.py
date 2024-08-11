from collections import defaultdict
from typing import List


def get_errors(s):
    error_codes = []
    nodes = s.split(" ")
    # 2 Duplicate check. O(N)
    set_nodes = set(nodes)
    if len(nodes) != len(set_nodes):
        error_codes.append(2)

    parents_map = defaultdict(list)
    children_map = defaultdict(list)
    nodes_list = set()
    for node in nodes:
        parents_map[node[1]].append(node[3])
        children_map[node[3]].append(node[1])
        nodes_list.add(node[1])
        nodes_list.add(node[3])

    # 3 Children check. O(N)
    for node, children in parents_map.items():
        if len(children) > 2:
            error_codes.append(3)

    # 4 Parents check O(N)
    for child, parents in children_map.items():
        if len(parents) > 2:
            error_codes.append(4)

    # 5 Tree Contains Cycle. O(N)
    roots = [node for node in nodes_list if node not in children_map.keys()]

    queue: List[str] = roots
    visited = set()

    while len(queue) > 0:
        node = queue.pop(0)
        if node in visited:
            error_codes.append(5)
            break
        visited.add(node)
        queue.extend(parents_map[node])

    return error_codes


print(get_errors("(A,B) (A,C) (B,D) (D,C) (A,E) (A,B)"))
print(get_errors("(A,B) (A,C) (B,D) (D,C)"))
