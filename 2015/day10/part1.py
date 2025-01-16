
def look_and_say(p_input, times):
    for x in range(times):
        print(x)
        result = ""
        idx = 0
        while idx < len(p_input):
            number = p_input[idx]
            repeat = 1
            for i in range(idx + 1, len(p_input)):
                if p_input[i] != number:
                    break
                idx += 1
                repeat += 1
            idx += 1
            result += str(repeat) + str(number)
        p_input = result
    return result



if __name__ == "__main__":
    print(len(look_and_say("1113122113", 40)))