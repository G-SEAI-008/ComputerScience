print("task 1")
num = 0
if num < 0:
    print("number is negative")
elif num == 0:
    print("number is 0")
else:
    print("number is positive")


print("task 2")
score = 80

if score > 90:
    print("A")
elif score > 80:
    print("B")
elif score > 70:
    print("C")
elif score > 60:
    print("D")
elif score > 50:
    print("E")
else:
    print("F")


print("task 3")

age = 13
status = "adult" if age >= 18 else "minor"
print(status)

print("task 4")
vehicles = ["bicycle", "car", "train", "plane", "ship"]

for vehicle in vehicles:
    print(f"Today I am taking the {vehicle}.")


print("task 5")
for i in range(1, 11):
    if i % 2 != 0:
        continue
    print(i)


print("task 6")
num = 0
sum = 0

while num <= 100:
    sum += num
    num += 1

print(sum)


print("task 7")
word_list = ["car", "fish", "watch", "dinosaur", "elephant", "tower"]

for word in word_list:
    if len(word) > 5:
        print(word)
        break


print("task 8")
people = ["Hannah", "John", "Karl"]
pets = ["Lucie", "Rex", "Mr. Whiskers"]

for person in people:
    for pet in pets:
        print(f"{person} loves {pet}")


print("task 9")

for item in people:
    if item == "Jim":
        print("Hello Jim")
        break
else:
    print("Hello Guest")

print("task 10")

for item in []:
    pass

fruits = ["apple", "banana", "orange", "mango"]
veggies = ["carrot", "broccoli", "spinach", "pepper"]
meat = ["chicken", "beef", "pork", "lamb"]

item = "mango"

match item:
    case _ if item in fruits:
        print(f"{item.capitalize()} is a fruit.")
    case _ if item in veggies:
        print(f"{item.capitalize()} is a vegetable.")
    case _ if item in meat:
        print(f"{item.capitalize()} is a meat product.")
    case _:
        print(f"{item.capitalize()} does not match any known category.")
