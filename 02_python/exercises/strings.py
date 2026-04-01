first_name = "Karl"
last_name = "Karlsen"

bio = """     I am instructor 
at the wbs coding school.
Currently I am teaching Python
"""

print(first_name[0])
print(last_name[-1])
print(bio[:10])

for char in first_name:
    print(char)

print(len(bio))

print("Python" in bio)
print("Java" in bio)

first_name = first_name.upper()
last_name = last_name.lower()
print(first_name)
print(last_name)

bio = bio.replace("Python", "coding").strip()
print(bio)

bio_list = bio.split(" ")
print(bio_list)


full_name = first_name + " " + last_name
print(full_name)

print(f"Hello, my name is {full_name} and I love Python!")

print("My full name is {} and I am {} years old".format(full_name, 35))

print('He said, "Python is great!"')

print(full_name.count("a"))

print(bio.center(100, "-"))
