class Time:
    """Represents the time of day.
    
    attributes: hour, minute, second
    """

def print_time(t):
    print('%.2d:%.2d:%.2d' % (t.hour, t.minute, t.second))


def is_after(t1, t2):
    return (t1.hour, t1.minute, t1.second) >  (t2.hour, t2.minute, t2.second)


t1 = Time()
t1.hour = 11
t1.minute = 59
t1.second = 30

t2 = Time()
t2.hour = 11
t2.minute = 8
t2.second = 55

print_time(t1)
print_time(t2)

print('Is t1 after t2? ' + ('Yes' if is_after(t1, t2) else 'No'))

