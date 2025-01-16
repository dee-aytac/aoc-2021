with open("input.txt", "r") as f:
	lines = f.readlines()

def task_2(lines):
	def checker(bitty, lines):
		for y in range(12):
			zerotot = 0
			onetot = 0
			for x in range(len(lines)):
				lines[x] = lines[x].strip("\n")
				if lines[x][y] == "0":
					zerotot += 1
				elif lines[x][y] == "1":
					onetot += 1
			if onetot > zerotot or zerotot == onetot:
				lines = [i for i in lines if i[y] == str(bitty)]
				if len(lines) == 1:
					return lines[0]
			elif zerotot > onetot:
				lines = [i for i in lines if i[y] == str(int(not bitty))]
				if len(lines) == 1:
					return lines[0]
	oxyRate = int(checker(1, lines), 2) 
	co2Rate = int(checker(0, lines), 2)
	print(oxyRate * co2Rate)

task_2(lines)