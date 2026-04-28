my_list = ["a", "b", "c"]

my_second_list = [1, 2, 3, 4, 5, 6, 7, 8]

# constant
print(my_list[0])


# linear

for el in my_list:
    print(el)
    print(el)


for x in my_list:
    for y in my_list:
        print(x, y)

for x in my_list:
    for y in my_second_list:
        print(x, y)
