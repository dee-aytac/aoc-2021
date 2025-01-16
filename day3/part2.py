import array as arr
oxygen_rates = []
co2_rates = []
with open('input.txt', 'r') as f:
    lines = f.read().splitlines()
    for line in lines:
        oxygen_rates.append(line)
        co2_rates.append(line)

while len(oxygen_rates) > 1:
    for i in range(len(oxygen_rates[0])):
        ones = 0
        zeros = 0
        for j in range(len(oxygen_rates)):
            if oxygen_rates[j][i] == str(1):
                ones += 1
            if oxygen_rates[j][i] == str(0):
                zeros += 1
        if ones > zeros or ones == zeros:
            drop = "0"
        else:
            drop = "1"
        list_length = len(oxygen_rates)
        l = 0
        while l < list_length:
            if oxygen_rates[l][i] == drop:
                oxygen_rates.pop(l)
                l -= 1
            list_length = len(oxygen_rates)
            l += 1
        if(len(oxygen_rates) == 1):
            break

while len(co2_rates) > 1:
    for i in range(len(co2_rates[0])):
        ones = 0
        zeros = 0
        print("len is", len(co2_rates))
        for j in range(len(co2_rates)):
            print(co2_rates[j])
            if co2_rates[j][i] == str(1):
                ones += 1
            if co2_rates[j][i] == str(0):
                zeros += 1
        if ones > zeros or ones == zeros:
            drop = "1"
        else:
            drop = "0"
        list_length = len(co2_rates)
        l = 0
        while l < list_length:
            if co2_rates[l][i] == drop:
                co2_rates.pop(l)
                l = l - 1
            list_length = len(co2_rates)
            l += 1
        if(len(co2_rates) == 1):
            break

oxygen_rating = int(oxygen_rates[0], 2)
co2_rating = int(co2_rates[0], 2)

        
print(oxygen_rating * co2_rating) # life support rating