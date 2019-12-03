
def call_number():
    for number in range(0, 10):
        print(number)


def call_number_whith_limit(b, limit):
    if b == 1:
        for number in range(limit):
            print(number)

    else:
        list = range(0, 10)
        for number in list[0: limit]:
            print(number)


print('function')
call_number()

print('\nfunction 2')
call_number_whith_limit(0, 50)
