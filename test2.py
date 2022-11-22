import os
import time

print(time.time())
print(time.ctime())

cur_time = time.ctime()
print(cur_time.split(" ")[-1])

for x in os.listdir('c:/anaconda3'):
    if x.endswith('exe'):
        print(x)


def mul(*value):
    sum = 0
    str = ''
    print("{} parameters.".format(value))
    for v in value:
        str += v

    return str


print(mul("javamix", "ohgilla"))