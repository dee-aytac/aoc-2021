
def solution(q_input):
    l = [0] * q_input
    for i in range(1, q_input):
        for j in range(i, min(i * 51, q_input), i):
            l[j] += i * 11
        if l[i] > q_input:
            return i

if __name__ == "__main__":
    print(solution(34000000))