import heapq
grid = []
for line in open('input.txt'):
    row = [int(char) for char in line.strip()]
    grid.append(row) 

rows = len(grid)
cols = len(grid[0])



que = [(0, 0, 0)]
heapq.heapify(que)
visited = set()
path = dict()
while que:
    distance, row, col = heapq.heappop(que)
    if (row, col) in visited:
        continue
    visited.add((row, col))
    path[(row, col)] = distance
    for (r, c) in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        rr = row + r 
        cc = col + c 
        if not ((0 <= rr and rr < rows * 5) and (0 <= cc and cc < cols * 5)):
            continue
        q1, r1 = divmod(rr, len(grid))
        q2, r2 = divmod(cc, len(grid[0]))
        distance_2 = (((grid[r1][r2] + q1 + q2) - 1) % 9) + 1
        real_distance = distance + distance_2
        heapq.heappush(que, (real_distance, rr, cc))
print(path[(499, 499)])
