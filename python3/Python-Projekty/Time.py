#!/usr/bin/env python3

#import time
# refatcor replace
# time.localtime
# time.strftime
# time.mktime
#
from time import localtime, strftime, mktime

start_time=localtime()
print(f"Twoj skrypt zaczol dzialac o: {strftime('%X',start_time)}")
input("Press ENTER to stop the Timer: ") 
stop_time=localtime()
diff = mktime(stop_time) - mktime(start_time)
print(f"Twoj skrypt skonczyl dzialac o: {strftime('%X',stop_time)}")
print(f"Skrypt dzialal przez: {diff} sec")