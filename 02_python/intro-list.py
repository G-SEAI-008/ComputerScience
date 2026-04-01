fruits = ["apple", "banana", "cherry"]

# print(fruits)
# print(type(fruits))

# print(fruits[-1])

# fruits.append("cucumber")
# # print(fruits)

# fruits[1] = "blueberry"
# # print(fruits)

# fruits.remove("cherry")


# fruits.append("cucumber")

# print(fruits)

# print(fruits[::2])

print("apple" in fruits)

# fruits.insert(2, "peach")
# print(fruits)

another_list = ["car", "bus", "tram"]


fruits.extend(another_list)

print(fruits)
# print(another_list)


element = fruits.pop(3)
print(type(element))
print(fruits)

fruits.clear()

print(fruits)


my_numbers = [1, 2, 3, 4, 5]
my_chars = ["a", "b", "c"]


# for char in my_chars:
#     print(char)

# for x in my_numbers:
#     print(x)
#     for y in my_numbers:
#         print(y)


def hi():
    print("hi")


def hello():
    print("hello")


fn_list = [hi, hello]

# for fn in fn_list:
#     fn()


alphabet = ["a", "b", "c", "d", "e"]


alphabet[1], alphabet[3] = alphabet[3], alphabet[1]

# print(alphabet)


nested_list = [1, [2, 3, [4, 5], 6, 7], 8]

# print(nested_list[1][2][1])


for x in nested_list:
    print(x)


print(range(1, 10))

for i in range(1, 10):
    print(i)


print(list(range(1, 10, 3)))


# list comprehension

# [expression, loop, condition]

range_list = ["hello" + " world" for i in range(1, 4)]

print(range_list)


new_number_list = [num for num in my_numbers if num > 3]
print(new_number_list)


new_alphabet = [char + char for char in alphabet]

print(new_alphabet)


letters = ["A", "B", "C"]

pairs = [x + y for x in letters for y in letters if x != y]


second_pairs = []
for x in letters:
    for y in letters:
        if x != y:
            second_pairs.append(x + y)

print(pairs)
print(second_pairs)


random_numbers = [5, 2, 3, 1, 9]

# random_numbers.sort()
sorted_list = sorted(random_numbers)

print(random_numbers)
print(sorted_list)


random_alphabet = ["b", "d", "f", "g", "G", "A"]
random_alphabet.sort(reverse=True)

print(random_alphabet)

print(ord("A"))

print(ord("a"))


my_best_list = ["karl", "hannah", "john", "gustav", "karla"]

my_best_list_b = my_best_list

my_best_list.append("jane")

print(my_best_list)
print(my_best_list_b)


my_best_list_c = my_best_list.copy()
my_best_list_C = my_best_list[:]


print(my_best_list == my_best_list_b)
print(my_best_list is my_best_list_b)


print(my_best_list_c == my_best_list)
print(my_best_list_c is my_best_list)


# first = my_best_list[0]
# second = my_best_list[1]

first, second, third, *rest = my_best_list

print(first)
print(second)
print(third)
print(rest)
