#Dates

import datetime

from datetime import datetime

now = datetime.now()
def print_date(date):
    print(date.day) 
    print(date.month)
    print(date.year)
    print(date.hour)
    print(date.minute)
    print(date.second)

print_date(now)
timestamp = now.timestamp()

print(timestamp)


#Setear tiempo
#Si no ponemos hora interpreta 00:00:00
year_2024 = datetime(2011,9,21)
print(year_2024)

from datetime import time
current_time = time()

print(current_time.hour)
print(current_time.min)
print(current_time.second)

from datetime import timedelta
from datetime import date
from datetime import time
from datetime import datetime
current_time = date(2011,9,21)
print(current_time.year)
print(current_time.month)
print(current_time.day)

print(current_time)

current_date = date(current_time.year, current_time.month + 1, current_time.day)
print(current_date.month)
now_date = now
print('---->',now)
diff = year_2024 - now_date
print('<------->',diff)
diff = year_2024.date() - current_date

print(diff)
