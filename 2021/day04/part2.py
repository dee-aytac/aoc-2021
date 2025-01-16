with open('sample.txt', 'r') as f:
    fx = f.read().split('\n')
    number_of_cards = (len(fx) - 1) // 6
    numbers = fx[0].split(',')
    fx = fx[1:]
    cards = []
    for i in range(0, number_of_cards):
        row = fx[i * 6 + 1:i * 6 + 6]
        row = [n.split() for n in row]
        row = [list(map(int,i)) for i in row]
        cards.append(row)


def start(cards):
    for number in numbers:
        for i in range(len(cards)):
            for j in range(len(cards[0])):
                for k in range(len(cards[i])):
                    if cards[i][j][k] == int(number):
                        cards[i][j][k] = 0
        if number == numbers[-1]:
            find_score(last_card, number)
            break
        last_card = check(cards, number)



def check(board, prev_number):
    to_remove = []
    last_card = None
    for i in range(len(cards)):
        for j in range(len(cards[0])):
            # Vertical check
            if (cards[i][0][j] + cards[i][1][j] + cards[i][2][j] + cards[i][3][j] + cards[i][4][j]) == 0:
                if len(cards) == 1:
                    find_score(cards[0], prev_number)
                to_remove.append(i)
                break
            # Horizontal check
            if cards[i][j][0] + cards[i][j][1] + cards[i][j][2] + cards[i][j][3] + cards[i][j][4] == 0:
                if len(cards) == 1:
                    find_score(cards[0], prev_number)
                to_remove.append(i)
                break
    for index in sorted(to_remove, reverse=True):
        last_card = cards[index]
        del cards[index]
    if last_card != None:
        return last_card


def find_score(card, prev_number):
    sum = 0
    for i in range(0, len(card)):
        for j in range(0, len(card[0])):
            sum += card[i][j]
    print(sum)
    print("found it!!", sum * int(prev_number))
    exit()

if __name__ == "__main__":
    start(cards)

