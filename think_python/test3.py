def do_twice(f, a):
    f(a)
    f(a)

def do_four(f, a):

    do_twice(f, a)
    do_twice(f, a)

def print_spam(a):
    print(a)
    

do_twice(print_spam, 'test')

do_four(print_spam, '4')
