import random


def greetPerson():
    print("Hello Person")


# greetPerson()


def greetPerson2(person):
    print(f"Hello {person}")


name = "Karl"
# greetPerson2(name)
# greetPerson2("Hannah")


def simple_add_numbers(a, b):
    print(a + b)
    return a + b


result = simple_add_numbers(5, 2)
# print(result)
# print(simple_add_numbers(5, 2))


# print(simple_add_numbers(2, b=5))


def just_positional_arguments(a, b, c, /):
    print(a, b, c)


# just_positional_arguments(1, 2, 3)


def just_keyword_arguments(*, a, b, c):
    print(a, b, c)


# just_keyword_arguments(b=3, c=4, a=5)


def combined_args(a, b, c, /, *, d):
    print(a, b, c, d)


# combined_args(1, 2, 3, d=4)


def greetPerson3(name="Guest", greeting=""):
    print(f"{greeting} {name}")


# greetPerson3("Karl", "Salut")
# greetPerson3()


def printNumbers(*args):
    print(type(args))
    for num in args:
        print(num)


# printNumbers(1)
# printNumbers(1, 2, 3, 4)
# printNumbers(1, 2, 3, 4, 5, 5, 2, 2, 34, 3)

# printNumbers()


def printNames(**kwargs):
    print(type(kwargs))
    for key in kwargs:
        print(kwargs[key])


# printNames(personA="John", personB="Jane", personC="Karl")


def print_result(B=0):
    print(f"The result is: {B}")


def addNumbers(a, b):
    A = a + b
    print_result(A)
    return A


# C = addNumbers(3, 4)


def format_full_name(name):
    return name.center(20, "*")


def reverse_full_name(name):
    return "".join(reversed(list(name)))


def uppercase_full_name(name):
    return name.upper()


def generate_full_name(first_name, last_name, *format_fn):
    full_name = f"{first_name} {last_name}"
    for fn in format_fn:
        full_name = fn(full_name)
    return full_name


# my_name = generate_full_name(
#     "karl",
#     "karlsen",
#     reverse_full_name,
#     uppercase_full_name,
#     format_full_name,
# )

# print(my_name)


def outer_function(fn, *args):
    print("I am the outer function")
    fn(*args)
    print("Told you")


# outer_function(greetPerson)

# outer_function(greetPerson2, "Karl")

# outer_function(simple_add_numbers, 2, 4)


def log_elements_bad(list, order_strategy):
    copy_list = list.copy()

    if order_strategy == "sorted":
        copy_list.sort()
    elif order_strategy == "reversed":
        copy_list.reverse()
    elif order_strategy == "random":
        random.shuffle(copy_list)

    for el in copy_list:
        print(el)


my_list = ["a", "b", "c", "d", "e"]


# log_elements_bad(my_list, "random")
# log_elements_bad(my_list, "reversed")


def sort_list(list):
    return sorted(list)


def reverse_list(list):
    return reversed(list)


def shuffle_list(list):
    copy_list = list.copy()
    random.shuffle(copy_list)
    return copy_list


def log_elements_better(list, order_strategy):
    ordered_list = order_strategy(list)
    for el in ordered_list:
        print(el)


# log_elements_better(my_list, shuffle_list)


# log_elements_better(my_list, lambda list: reversed(sorted(list)))


addNumbers3 = lambda x, y: x + y


def addNumbers4(x, y):
    return x + y


# print(addNumbers3(2, 3))


# my_number = 5


def multiply_by_n(multiplier):
    def multiply(number):
        return multiplier * number

    return multiply


def multiply_by_n_short(multiplier):
    return lambda number: multiplier * number


"""
def multiply(number):
    return 3 * number
"""

multiply_by_three = multiply_by_n(3)


# print(multiply_by_three(5))


# error handling


def divide_10_by_number(number):
    try:
        result = 10 / number
    except TypeError:
        print("That's not a valid number")
    except ZeroDivisionError:
        print("Cannot divide by zero")
    else:
        print(f"The result is {result}")
    finally:
        print("I always run")


# divide_10_by_number(2)

# divide_10_by_number(0)
# divide_10_by_number("10")


# print("do you see me?")


def get_user_input():

    try:
        user_input = int(input("Enter a number"))
    except Exception:
        print("You have to enter a number")
    else:
        print(f"You entered {user_input}")


get_user_input()
