def linecount(filename):
    count = 0
    for line in open(filename):
        count += 1
    return count

import os

#print(os.getcwd())
if __name__ == '__main__':
    print(linecount('wc.py'))