cars = {}
print(cars)

cars['corola'] = "red"
cars['up'] = "green"
cars['320'] = "black"

print("\ncars")
print(cars)

print("\nkey")
print(cars.keys())

print("\nValues")
print(cars.values())

people = dict(Wesley='Father', Maria='Mother', Sarah='baby')
print('\npeople')
print(people)

if 'Wesley' in people:
    print("\npeople['Wesley']")
    print(people['Wesley'])

for key, value in cars.items():
    print(key + " = " + value)
