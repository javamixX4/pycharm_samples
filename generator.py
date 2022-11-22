import time


def sleep_func(x):
    print("sleep_")
    time.sleep((1))
    return x

list = [sleep_func(x) for x in range(5)]
gen = (sleep_func(x) for x in range(5))

for i in list:
    print(i)

for i in gen:
    print(i)


