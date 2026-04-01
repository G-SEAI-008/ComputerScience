name = "Karl"
age = 28
height = 1.85

print(name)
print(age)
print(height)

print(type(name))
print(type(age))
print(type(height))

age_str = str(age)

# v1
print("My name is " + name + " and I am " + age_str + " years old.")

# v2
print(f"My name is {name} and I am {age_str} years old.")

global_message = "I am the world!"


def my_function():
    global global_message

    global_message = "You are not!"


my_function()
print(global_message)
