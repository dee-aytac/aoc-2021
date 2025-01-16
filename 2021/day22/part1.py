cubes = set()
for line in open('input.txt'):
    command = line.strip()
    if command[:2] == "on":
        x, y, z = command[3:].split(',')
        #print(x)
        x_low, x_high = x[2:].split('..')
        y_low, y_high = y[2:].split('..')
        z_low, z_high = z[2:].split('..')
        if (int(x_low) < -50 or int(x_high) > 50) or (int(x_low) < -50 or int(x_high) > 50) or (int(x_low) < -50 or int(x_high) > 50):
            print("What??")
            break
        for xx in range(int(x_low), int(x_high) + 1):
            for yy in range(int(y_low), int(y_high) + 1):
                for zz in range(int(z_low), int(z_high) + 1):
                    cubes.add((xx, yy, zz))
                    print("Adding", xx, yy, zz)
        print("-----------")
    else:
        x, y, z = command[4:].split(',')
        x_low, x_high = x[2:].split('..')
        y_low, y_high = y[2:].split('..')
        z_low, z_high = z[2:].split('..')
        if (int(x_low) < -50 or int(x_high) > 50) or (int(x_low) < -50 or int(x_high) > 50) or (int(x_low) < -50 or int(x_high) > 50):
            print("What?")
            break
        for xx in range(int(x_low), int(x_high) + 1):
            for yy in range(int(y_low), int(y_high) + 1):
                for zz in range(int(z_low), int(z_high) + 1):
                    if (xx, yy, zz) in cubes:
                        print("Removing", xx, yy, zz)

                        cubes.remove((xx, yy, zz))
                    #print(x, y, z)
        print("-----------")

print(len(cubes))