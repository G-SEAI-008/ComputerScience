import random

# print("hello world")

# # comments
# # this is my first comment

# """
# this is a multi-line comment
# """


# if 5 < 2:
#     print("5 is greater than 2")
#     print("something")
# else:
#     print("else")


# # variables
# _my_age = 50

# name = "Karl"
# Name = "Hannah"
# name = "Karla"
# name = 100

# print(name)
# print(Name)

# height = 5.6

# a, b, c = 1, 2, 3
# x = y = z = 10


# my_number = 10.2498844238

# print(int(round(my_number, 0)))

# int_height = int(height)
# print(int_height)

# str_age = str(_my_age)
# print(type(str_age))


# print("Hello")
# print("Salut")

# print("Hello, My age is " + str(_my_age))


# global_var = "I am global"


# def hi():
#     print("hi")


# def test_global():
#     local_variable = "salut"
#     global global_var
#     global_var = 10
#     print(global_var)


# test_global()
# print(global_var)

# print(local_variable)


# print("random")


# random_int = random.randint(1, 100)
# print(random_int)


# random_float = random.random()
# print(random_float)


# dice_roll = random.randint(1, 6)
# print(dice_roll)


# string

greeting = "hello world"

print(len(greeting))
# print(greeting[8])
# print(greeting[-3])
# for char in greeting:
#     print(char + "xx")

print("salut" not in greeting)

# print(greeting[0:4])
# print(greeting[3:])
# print(greeting[:4])

# print(greeting[2:-1:3])

# print(greeting[2:-1:2])

# print(greeting[::2])


# print("hello".upper())

# print("HELLO".lower())
# print("Hello".replace("l", "m"))

greeting = "hello"
greeting = greeting.replace("l", "m")

print(greeting)
# print(new_greeting)


first_name = "Karl"

age = 50

print("Hello " + first_name + "I am " + age + "years old")

print(f"Hello, I am {first_name} I am {age} years old.")
