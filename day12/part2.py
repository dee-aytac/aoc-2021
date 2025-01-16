from collections import defaultdict, deque

system = defaultdict(list)
for line in open('input.txt'):
    from_, to_ = line.strip().split('-')
    system[from_].append(to_)
    system[to_].append(from_)   
paths = 0
que = deque([('start', set(['start']), None)])
while que:
    current, visited, cave = que.popleft()
    if current == 'end':
        paths += 1
        continue
    for node in system[current]:
        if node not in visited:
            new_visited = set(visited)
            if node.lower() == node:
                new_visited.add(node)
            que.append((node, new_visited, cave))
        elif node in visited and  node != 'start' and node != 'end' and cave is None :
            que.append((node, visited, node))
print(paths)
