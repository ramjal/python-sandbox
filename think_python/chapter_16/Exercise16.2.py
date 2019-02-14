from datetime import datetime
from datetime import timedelta

def print_week_day():
    print('Today is ' + datetime.now().strftime('%A'))


def print_age(born):
    now = datetime.now()
    if datetime(now.year, born.month, born.day) <= now:
        nextBday = datetime(now.year + 1, born.month, born.day)
    else:
        nextBday = datetime(now.year, born.month, born.day)
    print(born.strftime('Birthday: %A, %d %B %Y'))
    age = now.year - born.year - ((now.month, now.day) < (born.month, born.day))
    print('Age:', age)
    delta = nextBday - now    
    days = delta.days
    hours, seconds = divmod(delta.seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    print('To next birthday: %d days, %d hours, %d minutes, %d seconds' % (days, hours, minutes, seconds))

# age in number of days
def days_age(born):
    return (datetime.now() - born).days


# print the day when d1 is twice as old as d2
def day_older_double(d1, d2):
    days1 = (datetime.now() - d1).days
    days2 = (datetime.now() - d2).days
    # make sure d1 is bigger
    if (days1 < days2):
        days1, days2 = (days2, days1)
    double = datetime.now() - timedelta(days=(days2 * 2 - days1))
    return(double)


# print the day when d1 is twice as old as d2
def day_n_time(d1, d2, n):
    days1 = (datetime.now() - d1).days
    days2 = (datetime.now() - d2).days
    # make sure d1 is bigger
    if (days1 < days2):
        days1, days2 = (days2, days1)
    diff = (days1 - n * days2) / (1 - n)
    double = datetime.now() - timedelta(days=diff)
    return(double)


print_week_day()
print_age(datetime(1962, 4, 18))
print('Days1 = ', days_age(datetime(1962, 4, 18)))
print('Days2 = ', days_age(datetime(1965, 9, 5)))
double = day_older_double(datetime(1962, 4, 18), datetime(1965, 9, 5))
print('Double Day = ', double.strftime('%Y-%m-%d'))
nTimes = day_n_time(datetime(1965, 9, 5), datetime(1962, 4, 18), 5)
print('5 Times Day = ', nTimes.strftime('%Y-%m-%d'))