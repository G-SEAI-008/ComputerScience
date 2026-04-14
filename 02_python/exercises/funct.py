def sum(list):
    sum = 0
    for num in list:
        sum += num
    return sum


print(sum((2, 3, 4, 5, 6)))


def repeat_greeting(name, times):
    for x in range(times):
        print(f"Hello {name}")


repeat_greeting("karl", 5)


def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result


print(factorial(5))


def fibonacci(n):
    sequence = [0, 1]
    if n <= 2:
        return sequence
    for x in range(2, n):
        sequence.append(sequence[x - 1] + sequence[x - 2])
    return sequence


print(fibonacci(10))


def max_of_two(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return "both are the same"


print(max_of_two(4, 5))
print(max_of_two(5, 5))


def print_triangle(rows):
    for x in range(1, rows + 1):
        for y in range(x):
            print("*", end="")
        print("")


def print_triangleB(row):
    for x in range(1, row + 1):
        print("*" * x)


# mirror
def print_triangleC(rows):
    for i in range(1, rows + 1):
        for j in range(rows - i):
            print(" ", end="")

        for k in range(i):
            print("*", end="")
        print()


# print_triangle(5)

# print_triangleB(5)

# print_triangleC(10)


def print_triangleD(rows):
    a = 1
    while a <= rows:
        print(a * "*")
        a += 1


print_triangleD(10)
