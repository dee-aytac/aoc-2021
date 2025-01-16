
def solution(q_input):
    q_input = q_input // 10
    l = [0] * q_input
    for i in range(1, q_input):
        for j in range(i, q_input, i):
            l[j] += i
        if l[i] > q_input:
            return i

if __name__ == "__main__":
    print(solution(34000000))

