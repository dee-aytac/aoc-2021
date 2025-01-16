from collections import defaultdict
with open('input.txt') as f:
  data = f.read()

data = data.splitlines()


def parse(line):
  parts = line.split(' ')
  return (parts[1], parts[7])

num = 5

def time(c):
  return 60 + ord(c) - 64

dep_pairs = defaultdict(lambda: [])
  
for line in data:
  f, s = parse(line)
  dep_pairs[s].append(f)
  dep_pairs[f]
  
done = []
tick = 0
workers = [-1 for _ in range(0,num)]
workingon = [None for _ in range(0,num)]

def get_work():
  for l, deps in sorted(dep_pairs.items()):
    if l not in done and all(d in done for d in deps) and l not in workingon:
      return l
    
  return None


while len(done) < len(dep_pairs) or any(w > tick for w in workers):  
  for i, w in enumerate(workers):
    if w <= tick:
      if workingon[i] is not None:
        done.append(workingon[i])
        workingon[i] = None
        
  for i, w in enumerate(workers):
    if w <= tick:
      work = get_work()
      if work is not None:
        workingon[i] = work
        workers[i] = time(work) + tick
        
  tick += 1
print(tick - 1)
print(done)