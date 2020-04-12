import time

ticks = time.time()

print('number of ticks since 12:00am, January 1, 1970: ' , ticks)

#lay thoi gian hien tai, cac ham: tm_year, tm_mon, tm_mday(1->31), tm_hour, tm_min, tm_sec, tm_wday(0->6), tm_yday(1->366)
print(time.localtime())

#thoi gian o dinh dang asctime()
print(time.asctime(time.localtime()))

#lich trong thang
import calendar

cal = calendar.month(2016, 2)
print('day la lich:')
print(cal)