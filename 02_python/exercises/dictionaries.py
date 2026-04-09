print("task 1")
person = {"name": "karl", "age": "30", "city": "paris"}

print(person)

print("task 2")
print(person["name"])
print(person.get("email", "not available"))
print(person.keys())
print(person.values())
print(person.items())


print('hello "world"')
print("hello 'world'")

print("task 3")
print("age" in person)


print("task 4")
person["city"] = "berlin"
print(person)
person.update({"city": "madrid", "age": 40, "email": "karl@madrid.de"})
print(person)

print("task 5")
person["country"] = "spain"
print(person)
person.update({"hobby": "cycling"})
print(person)

print("task 6")
print(person.pop("hobby"))
print(person)
print(person.popitem())
print(person)

del person["age"]
print(person)

# person.clear()
# print(person)

print("task 7")

copy_person = person.copy()
person["name"] = "john"

print(person)
print(copy_person)

print("task 8")

print(person.setdefault("city", "barcelona"))
print(person)
print(person.setdefault("book", "bible"))
print(person)
