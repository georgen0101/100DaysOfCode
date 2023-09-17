import time

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformated = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformated)
        time.sleep(1)
        time_sec -= 1



print(countdown(5))

