import collections
import heapq
grid = []
for line in open('input.txt'):
    row = [int(char) for char in line.strip()]
    print(row)
    grid.append(row) 
rows = len(grid)
cols = len(grid[0])
que = [(0, 0, 0)]
end = [(rows - 1, cols - 1)]
heapq.heapify(que)
visited = set()
path = dict()
while len(que):
    row, col, distance = heapq.heappop(que)
    if (row, col) in visited:
        continue
    if end[0] == row and end[1] == col:
        break
    visited.add((row, col))
    path[(row, col)] = distance
    for (r, c) in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        rr = row + r 
        cc = col + c 
        if not ((0 <= rr and rr < rows) and (0 <= cc and cc < cols)):
            continue
        if (rr, cc):
            heapq.heappush(que, (rr, cc, distance + grid[rr][cc]))
print(path)