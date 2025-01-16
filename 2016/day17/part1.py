from collections import deque
import hashlib

def solution(passcode, goal_x, goal_y):
    map_size = 4

    visited = set()
    steps = ""
    deq = deque()
    start_x, start_y = 0, 0
    deq.append((start_x, start_y, steps))
    visited.add((start_x, start_y))
    while True:
        pos = deq.popleft()
        current_x, current_y, steps = pos[0], pos[1], pos[2]
        if current_x == goal_x and current_y == goal_y:
            return steps

        for direction in ["D", "U", "R", "L"]:
            if direction == "D":
                current_x += 1
                check_index = 1
            elif direction == "U":
                current_x -= 1
                check_index = 0
            elif direction == "R":
                current_y += 1
                check_index = 3
            elif direction == "L":
                current_y -= 1
                check_index = 2
            if (current_x >= 0 and current_x < map_size) and (current_y >= 0 and current_y < map_size):
                hash_result = hashlib.md5((passcode+steps).encode()).hexdigest()
                if hash_result[check_index] in ["b", "c", "d", "e", "f"]:
                    deq.append((current_x, current_y, steps + direction))
                    visited.add((current_x, current_y))
            current_x, current_y = pos[0], pos[1]

if __name__ == "__main__":
    print(solution("qtetzkpl", 3, 3))