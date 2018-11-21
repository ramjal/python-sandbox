# input number and calculate
# the day and month of year.


day = int (input('Enter number:'))
Lenght_year = 365



if 0 < day <= 186:
    number_day = day % 31
    number_month = day // 31 + 1
    if day == 31:
        number_day = 31
        number_month = 1
    if day == 62:
        number_day = 31
        number_month = 2
    if day == 93:
        number_day = 31
        number_month = 3
    if day == 124:
        number_day = 31
        number_month = 4
    if day == 155:
        number_day = 31
        number_month = 5
    if day == 31:
        number_day = 31
        number_month = 6      
    
elif 186 < day <= Lenght_year:
    day -= 186
    number_day = day % 30
    number_month = day // 30 + 7
    if day == 216:
        number_day = 30
        number_month = 7
    if day == 246:
        number_day = 30
        number_month = 8
    if day == 276:
        number_day = 30
        number_month = 9
    if day == 306:
        number_day = 30
        number_month = 10
    if day == 336:
        number_day = 30
        number_month = 11
    if day == 365:
        number_day = 29
        number_month = 12
    
else:
    print ('your number is out of range')

print ('month is:',number_month, '\nday is:',number_day)