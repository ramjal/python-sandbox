
def is_triangle(a, b, c):
    if a > b+c or b > a+b or c > a+b:
        print('No')
    else:
        print('Yes')


print('Give me "a", "b", "c" one after eachother')
a = int(input())
b = int(input())
c = int(input())

is_triangle(a, b, c)

        
