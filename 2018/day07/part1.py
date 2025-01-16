from collections import defaultdict


def solution(fname):
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
    path += roots[0]
    if len(roots) > 1:
        other = roots[1]
    else:
        other = roots[0]
    visited = set()
    visited.add(roots[0])

    while True:
        visitable = list()
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
            next_step = visitable[0]
            path += next_step
            visited.add(next_step)
        if len(graph.keys()) + len(roots) == len(visited):
            break
    return path

if __name__ == "__main__":
    print(solution('input.txt')) 

