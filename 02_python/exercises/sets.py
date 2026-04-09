print("task 1")
fruits = {"banana", "apple", "orange", "cherry", "peach"}

print(fruits)

print("task 2")
print("apple" in fruits)

print("task 3")
fruits.add("date")
print(fruits)
more_fruits = {"papaya", "apricot", "kiwi"}

fruits.update(more_fruits)
print(fruits)


print("task 4")
fruits.remove("papaya")
print(fruits)
fruits.discard("watermelon")
print(fruits)
print(fruits.pop())
copied_fruits = fruits.copy()
print(copied_fruits)
copied_fruits.clear()
print(copied_fruits)

print("task 5")

set_a = {"peach", "kiwi", "date", "apricot", "mango"}
set_b = {"pineapple", "melon", "blackberry", "coconut", "kiwi", "date"}

print(set_a.union(set_b))
print(set_a.intersection(set_b))
print(fruits.intersection(set_a))

print(fruits.difference(set_b))
print(set_a.symmetric_difference(set_b))

print("task 6")
fruits.difference_update(set_a)
print(fruits)
set_a.intersection_update(set_b)
print(set_a)

fruits.update(set_b)
print(fruits)

print("task 7")
small_set = {3, 4, 5}
large_set = {2, 3, 4, 5, 6, 7, 8}

print(small_set.issubset(large_set))
print(large_set.issuperset(small_set))

print(small_set.isdisjoint(large_set))
