mapping = dict()
for idx, line in enumerate(open('input.txt', 'r')):
    if idx == 0:
        initial_text = line.strip()
    elif idx > 1:
        f, s = line.strip().split(' -> ')
        mapping[f] = s 

step = 10
for _ in range(step):
    new_text = ""
    for idx in range(len(initial_text) - 1):
        char = initial_text[idx:idx + 2]
        print(initial_text[idx] + initial_text[idx + 1])
        if idx == 0:
            new_text += initial_text[idx] + mapping[char] + initial_text[idx + 1]
        else:
            new_text +=  mapping[char] + initial_text[idx + 1]
    initial_text = new_text
print(initial_text)
import collections
most_common = collections.Counter(initial_text).most_common(1)[0][1]
least_common = collections.Counter(initial_text).most_common()[:-2:-1][0][1]
print(most_common - least_common)