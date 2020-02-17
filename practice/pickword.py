import random

fname = r'C:\DevLcl\Sandbox\python_sandbox\practice\sowpods.txt'
with open(fname) as fp:
    lines = fp.read().splitlines()

print("length = {}".format(len(lines)))
for i in range(4):
    print(random.choice(lines))