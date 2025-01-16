from collections import defaultdict
import string

def solution(fname, total_workers, delay):
    with open(fname, 'r') as f:
        content = f.read().strip().split('\n')
    graph = defaultdict(set)
    all_nodes = set()
    not_root = set()
    for line in content:
        info = line.split(' ')
        src = info[1]
        dest = info[-3]
        all_nodes.add(src)
        all_nodes.add(dest)
        not_root.add(dest)
        graph[dest].add(src)
    path = ""
    roots = [r for r in all_nodes.difference(not_root)]
    roots.sort()
    if len(roots) > 1:
        other = roots[1]
    else:
        other = roots[0]
    visited = set()
    alphabet = string.ascii_uppercase
    total_seconds = 0
    currently_visiting = dict()
    workers_left = total_workers
    while True:
        if len(graph.keys()) + len(roots) == len(visited):
            break
        visitable = list()
        if workers_left > 0:
            if roots[0] not in visited:
                visitable.append(roots[0])
            if other not in visited:
                visitable.append(other)
            for key in sorted(graph.keys()):
                val = graph[key]
                if key in visited:
                    continue
                can_visit = True
                for dep in val:
                    if dep not in visited:
                        can_visit = False
                if can_visit:
                    visitable.append(key)
            visitable.sort()
            if len(visitable) > 0:
                for next_step in visitable:
                    if next_step in currently_visiting.keys():
                        continue
                    workers_left -= 1
                    currently_visiting[next_step] = ord(next_step) - ord('A') + 1 + delay
                    if workers_left == 0:
                        break

        for key in list(currently_visiting.keys()):
            currently_visiting[key] -= 1
            if currently_visiting[key] == 0:
                path += key
                visited.add(key)
                workers_left += 1
                del currently_visiting[key]
        total_seconds += 1
    return path, total_seconds

if __name__ == "__main__":
    print(solution('input.txt', 5, 60)) 

