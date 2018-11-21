    
myDate = int(input('Enter a number\n'))
month = myDate // 30 + 1
day = myDate % 30
if day == 0: 
    day = 30
    month -= 1

print('The day is: %d and the month is: %d' % (day, month))



