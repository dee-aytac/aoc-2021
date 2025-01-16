
def get_next_char(char):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for idx in range(len(alphabet)):
        if alphabet[idx] == char:
            return alphabet[(idx + 1) % 26]

def is_valid_password(pw):
    if 'i' in pw or 'o' in pw or 'l' in pw:
        return False
    rule_2 = False
    for idx in range(len(pw) - 2):
        if pw[idx + 2] == get_next_char(pw[idx + 1]) and pw[idx + 1] == get_next_char(pw[idx]) and pw[idx+1] != 'a' and pw[idx+2] != 'a':
            rule_2 = True
    if rule_2 == False:
        return False
    repeats = 0
    for char in "abcdefghijklmnopqrstuvwxyz":
        pattern = char + char
        if pattern in pw:
            repeats += 1

    if repeats != 2:
        return False

    return True


def get_next_password(current_pw):
    while True:
        new_pw = list((current_pw[:7] + get_next_char(current_pw[7])).strip(" "))
        for idx in range(len(new_pw) - 1, 0, -1):
            if new_pw[idx] == 'a' and current_pw[idx] != 'a':
                new_pw[idx - 1] = get_next_char(new_pw[idx - 1])
        current_pw = "".join(new_pw)
        if is_valid_password(current_pw):
            return current_pw

if __name__ == "__main__":
    print(get_next_password("hxbxwxba"))