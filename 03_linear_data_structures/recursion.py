def format_string(string):
    return string.center(20, "*")


def generate_full_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    full_name = format_string(full_name)
    return full_name


# print(generate_full_name("karl", "karlsen"))


def sum(numbers):

    if len(numbers) == 1:
        return numbers[0]

    return numbers[0] + sum(numbers[1:])


sum([1, 2, 3, 4])


"""
sum([1,2,3,4]) -> 1 + sum([2,3,4])
sum([2,3,4]) -> 2 + sum([3,4])
sum([3,4]) -> 3 + sum([4])
sum([4]) -> 4
"""


def reverse_string(string):
    if len(string) == 1:
        return string

    result = reverse_string(string[1:]) + string[0]
    return result


reverse_string("hello")


"""
reverse_string("hello") -> reverse_string("ello") + "h"
reverse_string("ello") -> reverse_string("llo") + "e"
reverse_string("llo") -> reverse_string("lo") + "l"
reverse_string("lo") -> reverse_string("o") + "l"
reverse_string("o") -> o

"""
