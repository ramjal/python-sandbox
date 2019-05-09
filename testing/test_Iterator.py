""" 
Some testing on how an iterator works

"""

class OddNumbers:
    """ print odd nmbers """
    
    def __init__(self, max = 1):
        self.max = max

    def __iter__(self):
        self.n = 1
        return self

    def __next__(self):
        if self.n <= self.max:
            num = self.n
            self.n += 2
            return num
        else:                
            raise StopIteration


for k in OddNumbers(5):
    print(k)    

print('--------------------')

k = iter(OddNumbers(5))
print(next(k))
print(next(k))
