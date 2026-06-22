user_input_a = float(input("First number: "))
# user_input_b = input("Second number: ")

# number_a = float(user_input_a)
# # number_b = int(user_input_b)

# print(number_a + number_b)


def add_to_list(element, d_list=[]):
    d_list.append(element)
    print(d_list)


add_to_list("a")


my_list = []
add_to_list("c", my_list)
add_to_list("b")

print("hello world")
print("salut")


# if True:
#     break


# print("End")


# try:
#     print(5 / 0)
#     break
# except (ValueError, ZeroDivisionError):
#     print("too bad")
# except:
#     print("sorry")


count = 0
for i in range(2):
    for j in range(2):
        if i == j:
            count += 1
    else:
        count -= 1

print(count)


t = [[3 - i for i in range(3)] for j in range(3)]

[[3, 2, 1], [3, 2, 1], [3, 2, 1]]


s = 0
for i in range(3):
    s += t[i][i]

print(s)
