from collections import defaultdict, deque

system = defaultdict(list)
for line in open('input.txt'):
    from_, to_ = line.strip().split('-')
    system[from_].append(to_)
    system[to_].append(from_)   
paths = 0
que = deque([('start', set(['start']))])
while que:
    current, visited = que.popleft()
    if current == 'end':
        paths += 1
        continue
    for neighbour in system[current]:
        if neighbour not in visited:
            new_visited = set(visited)
            if neighbour.lower() == neighbour:
                new_visited.add(neighbour)
            que.append((neighbour, new_visited))
print(paths)

