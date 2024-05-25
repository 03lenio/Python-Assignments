import datetime
import time


def time_calc():
    while True:
        print(datetime.datetime.now()-datetime.datetime.strptime("21.03.1983 22:04:56", "%d.%m.%Y %H:%M:%S"))
        time.sleep(10)
        

time_calc()