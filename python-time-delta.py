# coding=utf-8

from datetime import datetime
import time

def time_delta(t1, t2):
    ts1 = datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
    ts2 = datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")
    d = ts1 - ts2
    return(int(d.total_seconds()) )



t1 = "Sun 10 May 2015 13:54:36 -0700"
t2 = "Sun 10 May 2015 13:54:36 -0000"


t1 = "Sat 02 May 2015 19:54:36 +0530"
t2 = "Fri 01 May 2015 13:54:36 -0000"



delta = time_delta(t1, t2)
print(delta)
