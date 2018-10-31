import math

def eval_loop():
    while True:
        s = input("Give me a string\n")
        if s == 'done':
            break
        else:
            print(eval(s))


eval_loop()


