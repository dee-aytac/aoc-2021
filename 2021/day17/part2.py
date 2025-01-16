# Runs under 6 seconds

def step(pos, vel):
    pos[0] += vel[0]
    pos[1] += vel[1]
    if vel[0] > 0:
        vel[0] -= 1
    elif vel[0] < 0:
        vel[0] += 1
    vel[1] -= 1 
    return pos, vel

def pass_target(borders, pos, vel):
    if pos[1] < borders['y']['lower']:
        return False
    elif (pos[0] > borders['x']['right'] and vel[0] > 0) or (pos[0] < borders['x']['left'] and vel[0] < 0):
        return False
    else:
        return True

def is_in(pos, borders):
    if (borders['x']['left']  <= pos[0] <= borders['x']['right']) and (borders['y']['lower']  <= pos[1] <= borders['y']['upper']):
        return True 
    return False 
 
def main():
    with open('input.txt') as f:
        content = f.read().split(' ')[2:]
        xs = list(map(int, content[0][2:].replace(',', '').split('..')))
        ys = list(map(int, content[1][2:].replace(',', '').split('..'))) 
    xs = sorted(xs)
    ys = sorted(ys)
    total_vels = 0
    borders = {'x': {'left': xs[0], 'right': xs[1]}, 'y': {'upper': ys[1], 'lower': ys[0]}}
    for x in range(-500, 500):
        for y in range(-500, 500):
            pos = [0, 0]
            vel = [x, y]
            while True:
                pos, vel = step(pos, vel)
                state = pass_target(borders, pos, vel)
                if state == False:
                    break
                inside = is_in(pos, borders)
                if inside:
                    total_vels += 1
                    break
    print(total_vels)
if __name__ == "__main__":
    main()