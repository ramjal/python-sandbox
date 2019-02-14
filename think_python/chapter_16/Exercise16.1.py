class Time:
    """Represents the time of day.
    
    attributes: hour, minute, second
    """

def print_time(t):
    print('%.2d:%.2d:%.2d' % (t.hour, t.minute, t.second))


def time_to_int(t):
    minutes = t.minute + t.hour * 60
    return t.second + minutes * 60


def int_to_time(n):
    time = Time()
    minutes, time.second = divmod(n, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


def mul_time(t, n):
    number = time_to_int(t) * n
    return int_to_time(number)


def time_per_mile(fin_time, dist):
    return mul_time(fin_time, 1/dist)

t1 = Time()
t1.hour = 1
t1.minute = 45
t1.second = 30

print(time_to_int(t1))
print_time(int_to_time(4230))
#print_time(mul_time(t1, 2))
print_time(time_per_mile(t1, 2))




    
