with open('input.txt', 'r') as f:
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
        found = check(cards, number)
        if found == True:
            break

def check(board, prev_number):
    for i in range(len(cards)):
        for j in range(len(cards[0])):
            # Vertical check
            if (cards[i][0][j] + cards[i][1][j] + cards[i][2][j] + cards[i][3][j] + cards[i][4][j]) == 0:
                card = cards[i]
                find_score(card, prev_number)
                return True
            # Horizontal check
            if cards[i][j][0] + cards[i][j][1] + cards[i][j][2] + cards[i][j][3] + cards[i][j][4] == 0:
                card = cards[i]
                find_score(card, prev_number)
                return True

def find_score(card, prev_number):
    sum = 0
    for i in range(0, len(card)):
        for j in range(0, len(card[0])):
            sum += card[i][j]
    print("found it!!", sum * int(prev_number))

start(cards)

