#-*- encoding: utf-8 -*-
import time


def now():
    time_str = time.strftime('%Y-%m-%d %H:%M:%S')
    return time_str


if __name__ == '__main__':
    t = now()
    print(t)
