def count_fishes(fishes, days):
    for i in range(days):
        new_fishes = 0
        for idx, num in enumerate(fishes):
            if fishes[idx] == 0:
                fishes[idx] = 6
                new_fishes += 1
            else:
                fishes[idx] -= 1
        for i in range(new_fishes):
            fishes.append(8)
    print(len(fishes))

def get_initial():
    with open('input.txt', 'r') as f:
        f_ = f.read().split(',')
        f_ = [int(i) for i in f_]
        print(f_)
        return f_

if __name__ == "__main__":
    initial_state = get_initial()
    count_fishes(initial_state, 80)