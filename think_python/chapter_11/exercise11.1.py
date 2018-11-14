fin = open(r'C:\DevLcl\Sandbox\python-sandbox\think_python\words.txt')

worldDict = {}

def populate_dict():    
    for line in fin:
        worldDict[line.strip()] = '?'


def find_word(w):
    if w in worldDict:
        print('found => %s' % w)
    else:
        print('not found => %s' % w)




populate_dict()
find_word('hasan')
find_word('test')
