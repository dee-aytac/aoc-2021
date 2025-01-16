def count_fishes(fishes, days):
    for i in range(days):
        new_fishes = fishes['0']
        for i in range(0, 8):
            fishes[str(i)] = fishes[str(i + 1)]
        fishes['8'] = new_fishes
        fishes['6'] += new_fishes
    total_fishes = 0
    for key in fishes.keys():
        total_fishes += fishes[key]
    print(total_fishes)

def get_initial():
    with open('input.txt', 'r') as f:
        f_ = f.read().split(',')
        dict_ = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0}
        for n in f_:
            dict_[n] +=1
        print(dict_)
        return dict_

if __name__ == "__main__":
    initial_state = get_initial()
    count_fishes(initial_state, 256)