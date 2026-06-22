# Jedes Problem soll vorrangig rekursiv gelöst werden auch wenn ein Loop manchmal die bessere Wahl wäre. D.h. jede Lösung muss mind. einmal eine Funktion beinhalten, die sich selbst aufruft. Loops sind nicht strikt verboten.

# Rekursion: base case, pre-condition, recursive call, post-condition


print("Aufgabe - Countdown")


# Countdown: Schreibe eine Function, die die Zahlen von n bis 1 ausgibt und am Ende "Liftoff" druck
def countdown(n):
    if n == 1:
        print(n)
        print("Liftoff")
    else:
        print(n)
        countdown(n - 1)


countdown(10)

print("\Aufgabe - Summe")


# Summe: Erstelle eine Funktion, die die Summe aller Zahlren von 1 bis n berechnet
def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n - 1)


print(sum(5))

print("\Aufgabe - Faktor")


# Fakultät: Erstelle eine Funktion, die die Faktultät einer Zahl ausrechnet
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))


print("\Aufgabe  - String umkehren")


# String umkehren: Erstelle eine Funktion. die einen String umdreht: "hello" -> "olleh"
def reverse_string(string):
    if len(string) == 1:
        return string
    else:
        return string[-1] + reverse_string(string[:-1])


print(reverse_string("hello"))

print("\n Aufgabe - Fibonacci")


# Fibonacci: Schreibe eine Funktion, um die n-te Fibonaccizahl zu finden.
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))

print("\n Aufgabe - Summe einer Liste")


# Summe einer Liste: Schreibe eine Funktion, die alle Elemente in einer Liste summiert
def sum_list(items):
    if not items:
        return 0
    return items[0] + sum_list[1:]


print("\n Aufgabe - Palindrom")


# Palindrom: Erstelle eine Funktion, die überprüft, ob ein Wort ein Palindrom ist: True: level, racecar, radar || False: hello, ship, fish
def is_palindrome(string):
    if len(string) <= 1:
        return True
    if string[0] != string[-1]:
        return False
    return is_palindrome(string[1:-1])


print(is_palindrome("racecar"))
print(is_palindrome("hello"))


print("\n Aufgabe - Spiegeldrucker")
# Spiegeldrucker: Erstelle eine Funktion, die von n herabzählt und anschließend wieder zu n hochzählt:
# 3 -> 3,2,1,2,3
# 5 -> 5,4,3,2,1,2,3,4,5


def mirror_printer(n):
    if n <= 1:
        print(n)
        return
    print(n)
    mirror_printer(n - 1)
    print(n)


mirror_printer(3)
mirror_printer(10)


print("\n Aufgabe - Höhlenforscher")
# Höhlenforscher: Erstelle eine Funktion, die visualiert, wie eine Figur n-Level hinabsteigt und n-Level wieder hochsteigt. Beachte die Einrückungen
# level_to_reach = 3
# current = 1
"""
Abstieg Level 1
    Abstieg Level 2
        Abstieg Level 3
        Aufstieg Level 3
    Aufstieg Level 2
Aufstieg Level 1
"""


def cave_explorer(level_to_reach, current):
    if current > level_to_reach:
        return
    compose_string = f"{"\t" * (current-1)} Abstieg Level {current}"
    print(compose_string)
    cave_explorer(level_to_reach, current + 1)
    compose_string = f"{"\t" * (current-1)} Aufstieg Level {current}"
    print(compose_string)


cave_explorer(3, 1)


print("\n Aufgabe - Ziffern zählen")


# Ziffern zählen: Schreibe eine Funktion, die die Ziffern einer Ganzzahl zählt
def count_digits(n):
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)


print(count_digits(203))
print(count_digits(53203))


print("\n Aufgabe - Summe verschachtelte Liste")


# Schreibe eine Funktion, die alle Zahlen in einer tiefer verschachtelten Liste summiert.
# [1, [2,3, [3,4], 2],12]
def nested_sum(lst):
    total = 0
    for element in lst:
        if isinstance(element, list):
            total += nested_sum(element)
        else:
            total += element
    return total


print(nested_sum([1, [2, 3, [3, 4], 2], 12]))


print("\n Aufgabe- Binary Search")
# Implementiere binary search rekursiv


def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    return -1


print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 0, 14, 11))

print("\n Aufgabe - Echo")
# Echo: Nehme einen String der Stück für Stück verkleinert wird (jeweils 1. Buchstaben entfernen) und am Ende wieder Stück für Stück zusammengestzt wird, aber dieses Mal mit Großbuchstaben
"""
hello
ello
llo
lo
o
O
LO
LLO
ELLO
HELLO
"""


def echo(word):
    if not word:
        return ""
    print(word)

    result = echo(word[1:])
    transformed = word[0].upper()

    print(transformed + result)
    return transformed + result


echo("hello")
