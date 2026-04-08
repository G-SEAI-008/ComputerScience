person = {
    "name": "Alice",
    "age": 40,
    "pets": ["dog", "cat"],
    "isMarried": False,
    "location": {"city": "madrid", "street": "calle de madrid", "country": "spain"},
}

settings = {"dark_mode": True}

person["pets"].append("bird")
# print(person)

# print(person["age"])
# print(person["pets"][0])

# print(person["location"]["city"])


# for pet in person["pets"]:
#     print(pet)


# print(person.keys())
# print(person.values())
# print(person.items())


# for key in person.keys():
#     print(key)


person["isMarried"] = True

person["email"] = "alice@example.org"

# del person["pets"]
# del person["test"]

# print(person.pop("test", "not found"))

# person.pop("age")
# print(person.popitem())

# print(person["recipe"])

recipe = person.get("recipe", "not defined")

# print(person.get("location", {}).get("country", "not found"))

# print(recipe)
# print(person)


# print("pets" in person)
# print("test" in person)


copy_person = person.copy()
copy_person2 = dict(person)


person["name"] = "karla"

person["location"]["city"] = "berlin"


# print("person")
# print(person)
# print("copy")
# print(copy_person)


stock = [
    {"id": 1, "name": "chocolate", "price": 1.50, "amount": 0},
    {"id": 2, "name": "drink", "price": 1.00, "amount": 40},
    {"id": 3, "name": "fruit", "price": 0.75, "amount": 10},
]

print("Item: \t Price")
for item in stock:
    if item["amount"] > 0:
        print(f"{item["name"].capitalize()} - {item["price"]:.2f}€")
