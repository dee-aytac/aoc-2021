import collections
mapping = dict()
chars = dict()
chars_2 = dict()
for idx, line in enumerate(open('input.txt', 'r')):
    if idx == 0:
        initial_text = line.strip()
        for idx in range(len(initial_text) - 1):
            char = initial_text[idx:idx + 2]
            if char not in chars:
                chars[char] = 1
            else:
                chars[char] += 1
    elif idx > 1:
        f, s = line.strip().split(' -> ')
        mapping[f] = s

print(chars)
step = 40
char_count = collections.Counter(initial_text)
for _ in range(step):
    for (c1, c2), value in chars.copy().items():
        nc = mapping[c1 + c2]
        chars[c1 + c2] -= value
        if c1 + nc not in chars:
            chars[c1 + nc] = 0
        chars[c1 + nc] += value
        if nc + c2 not in chars:
            chars[nc + c2] = 0
        chars[nc + c2] += value
        
        char_count[nc] += value

print(max(char_count.values()) - min(char_count.values()))