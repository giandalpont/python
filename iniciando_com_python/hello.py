def hello():
    return "Hello world"


print(hello())


def sam(e, r):
    return e + r


print(sam(3, 6))

number = [1, 1, 2, 3, 4]
number2 = [23, 23, 12, 112, 9]

print(number)
print(number2)
num = number + number2
print(num)

print(number[1])
print(number[2])
print(number[:3])

mix = [1, 2, '3', [1, 2, 3]]
print(mix)
print(mix[3][2])


numbers = [0, 1, 2, 4]
print(numbers)
numbers.append(8)  # add
numbers.append(8)  # add
print(numbers)
numbers.remove(8)  # remove remove somente o primeiro
print(numbers)
del(numbers[4]) # deletando pelo índice
print(numbers)
