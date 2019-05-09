def OddNumbers(max):
    n = 1
    while n <= max:
        print('Yielding %d' % (n))
        yield n
        n += 2


for n in OddNumbers(10):
    print(n)


def all_even():
    n = 0
    while True:
        yield n
        n += 2


for n in all_even():
    print(n)
    if n > 20:
        break