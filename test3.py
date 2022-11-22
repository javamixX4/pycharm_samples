def test():
    print("함수가 호출되었습니다.")
    yield "test"

print("A pass")
next(test())

print("B pass")
next(test())

print(test())


numbers = [1,2,3,4,5,6]
print("::".join(map(str,numbers)))
print("::".join(str(numbers)))

a = list(map(str, numbers))
print(a)

numbers2 = list(range(1, 10+1))
print("ODD number!!!")
print(list(filter(lambda x : x % 2 == 1, numbers2)))