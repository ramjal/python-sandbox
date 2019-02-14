
class Kangaroo:
    def __init__(self, name, contents=None):
        self.name = name
        if contents == None:
            contents = list()
        self.pouch_contents = contents

    def put_in_pouch(self, obj):
        self.pouch_contents.append(obj)

    def __str__(self):
        t = [ self.name + ' has pouch contents:' ]
        for obj in self.pouch_contents:
            s = '\t' + obj.__str__()
            #s = '\t' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)


def main():
    kanga = Kangaroo('Kanga')
    roo = Kangaroo('Roo')

    kanga.put_in_pouch(1)
    kanga.put_in_pouch('Ramin')
    kanga.put_in_pouch(354)
    kanga.put_in_pouch('Testing now!')
    kanga.put_in_pouch(roo)

    roo.put_in_pouch(123)
    roo.put_in_pouch(455)

    print(kanga)
    print(roo)

if __name__ == '__main__':
    main()
