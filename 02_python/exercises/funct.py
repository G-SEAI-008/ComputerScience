def sum_list(numbers):
    sum = 0
    for num in numbers:
        sum += num
    return sum


print(sum_list([1, 2, 3, 4, 5]))


def sum_list_b(limit):
    sum = 0
    for num in range(limit):
        sum += num
    return sum


print(sum_list_b(100))

print(sum_list_b(6))
