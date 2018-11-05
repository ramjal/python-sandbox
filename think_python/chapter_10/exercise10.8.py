import random

def has_duplicates(my_list):
    lcopy = my_list[:]
    lcopy.sort()
    for i in range(len(lcopy)-1):
        if lcopy[i] == lcopy[i+1]:
            return True
    return False


def birthday_paradox():
    students = []
    for i in range(23):
        students.append(random.randint(15, 99))
    # print(students)
    # students.sort()
    # print(students)
    return has_duplicates(students)


probability = 0
for i in range(1, 100):
    if birthday_paradox() == True:
        probability += 1  


print('Probability is %%%d' % probability)

# print(birthday_paradox())