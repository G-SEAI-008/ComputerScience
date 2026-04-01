print("task 1")
my_list = ["orca", "humpback whale", "hammerhead shark", "ocean sunfish", "stingray"]


print(my_list)


print("task 2")

print(my_list[0])
print(my_list[4])
print(my_list[-2])

print("task 3")
print(my_list[1:4])
print(my_list[:2])
print(my_list[2:])

print("task 4")
print("apple" in my_list)

print("task 5")
my_list.append("salmon")
my_list.insert(2, "tuna")
print(my_list)

print("task 6")
my_list[1:3] = ["shrimp", "catfish"]
print(my_list)

print("task 7")
my_list.remove("catfish")
print(my_list)
my_list.pop(5)
print(my_list)
# my_list.clear()
# print(my_list)

print("task 8")
copy = my_list.copy()
my_list[0] = "shoebill"
print(my_list)
print(copy)

print("task 9")
list_a = [1, 2, 3]
list_b = [4, 5, 6]
combined_list_a = list_a + list_b
print(combined_list_a)
print(list_a)
print(list_b)
list_a.extend(list_b)
print(list_a)
print(list_b)

print("task 10")
my_list.sort()
print(my_list)
my_list.reverse()
print(my_list)

print("task 11")
print(my_list.count("shoebill"))
print(my_list.index("ocean sunfish"))

print("task 12")

new_list = [animal.capitalize() for animal in my_list if animal[0] == "s"]
print(new_list)
