"""
Write a script that reads the current time and converts it to a time of day in hours, minutes, and
seconds, plus the number of days since the epoch.

"""
import time

print('**** started ****')
seconds_in_a_day = 24 * 60 * 60

the_time = time.time()
print('time:', the_time)

days = the_time // seconds_in_a_day
print('days: ', days)

total_seconds_today = int(the_time % seconds_in_a_day)
print('seconds_today: ', total_seconds_today)

hours_today = (total_seconds_today // 3600) - 8 + 1 - 12 # +1 is for summer time
print('hours_today: ', hours_today)

minutes_today = int((total_seconds_today % 3600) / 60)
print('minutes_today: ', minutes_today)

seconds_today = (total_seconds_today % 3600) % 60
print('seconds_today: ', seconds_today)

print('Current time Vancouver: ' 
        + str(hours_today) + ':' 
        + str(minutes_today) + ':' 
        + str(seconds_today))