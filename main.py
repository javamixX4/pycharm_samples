list_a = [1, 2, 3, 4, 5]
list_b = reversed(list_a)

print("List Reversed :", list(list_b))

for i in reversed(list_a):
    print("-", i)

for i in reversed(list_a):
    print("역배치 : {}".format(i))

for i in reversed(list_a):
    print("두번째 : {}".format(i))

def generator(n):
    i = 0
    while i < n:
        print("return {}".format(i))
        yield i
        i += 1
    print("generator function END")

for x in generator(5):
    print(x)