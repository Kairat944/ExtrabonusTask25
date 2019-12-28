numbers = input("Введите число:")
num_ = list(numbers.split(' '))
chet = []
nechet = []
for i in (num_):
    if int(i) % 2 == 0:
        chet.append(num_)
    else:
        nechet.append(num_)
print(len(chet),len(nechet))