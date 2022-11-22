example_list = ['eA', 'eB', 'eC']

print(enumerate(example_list))
print(list(enumerate(example_list)))

for i, value in enumerate(example_list):
    print("{}번째 요소는 {}이다.".format(i, value))

array = []
for i in range(0, 20, 2):
    array.append(i*i)

print(array)

arrayb = [i*i for i in range(0,20,2)]
print(arrayb)


test = (
    "나는 대한민국\n "
    "경기도 시흥시 "
    "네이처하임에 살고있다"
)

print(test)
print(type(test))

print("::".join(["1", "2",'3',"4"]))
print("{:b}".format(4))
print("{:o}".format(10))
print("{:x}".format(15 ))