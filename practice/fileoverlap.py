import os

fileName1 = os.path.join(os.getcwd(), 'happynumbers.txt')
fileName2 = os.path.join(os.getcwd(), 'primenumbers.txt')
l1 = []
l2 = []

def findOverlap(l1, l2):
    return sorted(set([x for x in l1 if x in l2]))

def putFileDataIntoList(fileName, l):
    with open(fileName, 'r') as open_file:
        while True:
            line = open_file.readline().rstrip('\n')
            if line:
                l.append(line)
            else:
                break


if __name__ == "__main__":
    putFileDataIntoList(fileName1, l1)
    putFileDataIntoList(fileName2, l2)
    print(findOverlap(l1, l2))