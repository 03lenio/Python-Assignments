import datetime
import time


def clock():
    while True:
        time.sleep(2)
        now = datetime.datetime.now()
        print(now.time())

clock()
