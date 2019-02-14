
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return 'Point is located at: x=%g, y=%g' % (self.x, self.y)

    def __add__(self, other):
        if isinstance(other, Point):
            return self.add_point(other)
        elif isinstance(other, tuple):
            return self.add_tuple(other)
        else:
            raise TypeError(type(other), "data type is now supported for the 'other' object")

    def __radd__(self, other):
        return self.__add__(other)

    def add_point(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def add_tuple(self, tup):
        self.x += tup[0]
        self.y += tup[1]
        return self

    def __lt__(self, other):
        if self.x < other.x and self.y < other.y:
            return True
        else:
            return False


##############################################
def print_attributes(obj):
    for attr in vars(obj):
        print(attr, getattr(obj, attr))

# p = Point(2, 3)
# p1 = Point(10, 10)
# print(p)
# print(p1)
# print('p is less than p1:', p > p1)    
# print(p + p1)        

p = Point(2, 3)
p1 = Point(10, 10)
p2 = Point(100, 200)
p3 = Point(2000, 3000)
all = sum([p, p1, p2, p3], Point(0,0)) # we should give sum a valid Point to start otherwies is passes 'int=0'
total = p + p1 + p2 + p3
print('total point:', total)

print_attributes(p)
print(vars(p))


# print('try:')
# try:
#     p = Point(2, 3)
#     print(p + (100, 200))
#     p = Point(2, 3)
#     print(p + 100, 200)
# except Exception as e:
#     print(e)

