"""
Exercise 5.2. Fermat’s Last Theorem says that there are no positive integers a, b, and c such that
an + bn = cn
for any values of n greater than 2.
1. Write a function named check_fermat that takes four parameters—a, b, c and n—and
checks to see if Fermat’s theorem holds. If n is greater than 2 and
an + bn = cn
the program should print, “Holy smokes, Fermat was wrong!” Otherwise the program should
print, “No, that doesn’t work.”
2. Write a function that prompts the user to input values for a, b, c and n, converts them to
integers, and uses check_fermat to check whether they violate Fermat’s theorem.

"""

def check_fermat(a, b, c, n):

    if (n <= 2):
        print('error: n smaller than 2')
        return
    
    left = a**2 + b**2 
    right = c**2

    if left == right:
        print('Holy smokes, Fermat was wrong!')
    else:
        print('No, that doesn’t work.')



print('give me "a"')
a = int(input())

print('give me "b"')
b = int(input())

print('give me "c"')
c = int(input())

print('give me "n"')
n = int(input())

check_fermat(a, b, c, n)

