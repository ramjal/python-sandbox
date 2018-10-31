import math

def mysqrt(a):
    x = a
    while True:
        if x <= 0:
            break
        #print(x)
        y = (x + a/x) / 2
        if y == x:
            return y
            break
        x = y

def test_square_root(a):
    for a in range(1, 3):
        sqr = mysqrt(a)
        msq = math.sqrt(a)
        print('%f %f %f %E' % (a, sqr, msq, abs(sqr - msq)))
        # print('a: ', a)
        # print('result: ', sqr)
        # print('math.sqrt: ', msq)
        # print('diff: ', abs(sqr - msq))


test_square_root(5)