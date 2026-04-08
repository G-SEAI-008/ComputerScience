my_set = {"orca", "dolphin", "stingray"}


print("Initial set:", my_set)


# for item in my_set:
#     print(item.capitalize())

# my_set.add("humpback whale")
# my_set.add("humpback whale")


# my_set.remove("dolphin")
# my_set.remove("shark")
# my_set.discard("dolphin")


print("orca" in my_set)


my_second_set = {"shark", "cuttlefish", "turtle"}


my_set.update(my_second_set)

# print(my_set)
# print(my_second_set)

result = my_set.pop()

# print(result)

my_set.clear()

# print(my_set)


first_set = {"a", "b", "c", "d", "e"}
second_set = {"d", "e", "f", "g", "h"}


# print("union")
# print(first_set.union(second_set))


# print("intersection")
# print(first_set.intersection(second_set))


# print("difference")
# print(first_set.difference(second_set))
# print(second_set.difference(first_set))


# print("symmetric difference")
# print(first_set.symmetric_difference(second_set))


# print("intersection update")

# first_set.intersection_update(second_set)
# print(first_set)
# print(second_set)


print("disjoint")
print(first_set.isdisjoint(second_set))

print("subset")
print(first_set.issubset(second_set))
print("superset")
print(first_set.issuperset(second_set))


set_a = {4, 5, 6, 7}
set_b = {4, 5, 6}


print(set_a > set_b)
