# if the two numbers print opposits like 34 and 43
def is_reverse_numbers(number1, number2):
    # print(number1, number2)
    if str(number1).zfill(2)[::-1] == str(number2).zfill(2):        
        # print('', number1, number2)
        return True


def check_is_reserve(diff):
    count = 0
    for i in range(1, 99):
        if (is_reverse_numbers(i, i + diff)):
            count += 1
    if count > 0:
        print('diff:', diff, 'count: ', count)



# check_is_reserve(18)
for diff in range(15, 60):
    check_is_reserve(diff)
