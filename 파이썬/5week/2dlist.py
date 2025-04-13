print("# 한번 반복")
list_of_list = [
    [1, 2, 3],
    [4, 5, 6, 7],
    [8, 9]
]

for items in list_of_list:
    print(items)

print("# 두번 반복")
list_of_list = [
    [1, 2, 3],
    [4, 5, 6, 7],
    [8, 9]
]

for items in list_of_list:
    for item in items:
        print(items)