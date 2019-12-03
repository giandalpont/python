list = [1, 2, 3, 4, 5, 6, 7]

print("for 1")
for item in list:
    if item > 2:
        if not item == 5:
            print(item)

print("\nfor 2")

for item in list[0:2]:
    print(item)
