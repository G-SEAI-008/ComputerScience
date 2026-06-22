# Jedes Problem soll vorrangig rekursiv gelöst werden, auch wenn ein Loop manchmal die bessere Wahl wäre. D.h. jede Lösung muss mind. einmal eine Funktion beinhalten, die sich selbst aufruft. Loops sind nicht strikt verboten.

# Denkt über folgende Elemente einer Rekursion nach:
# base case, pre-condition, recursive call, post-condition


print("Aufgabe - Countdown")

# Countdown: Schreibe eine Function, die die Zahlen von n bis 1 ausgibt und am Ende "Liftoff" druckt.
def countdown(n):
    pass


countdown(10)

print("\nAufgabe - Summe")

# Summe: Erstelle eine Funktion, die die Summe aller Zahlen von 1 bis n berechnet.
def sum(n):
    pass


print(sum(5))

print("\nAufgabe - Fakultät")

# Fakultät: Erstelle eine Funktion, die die Faktultät einer Zahl ausrechnet.
def factorial(n):
    pass


print(factorial(5))


print("\nAufgabe - String umkehren")

# String umkehren: Erstelle eine Funktion, die einen String umdreht: "hello" -> "olleh"
def reverse_string(string):
    pass


print(reverse_string("hello"))

print("\nAufgabe - Fibonacci")

# Fibonacci: Schreibe eine Funktion, um die n-te Fibonaccizahl zu finden.
def fibonacci(n):
    pass


print(fibonacci(10))

print("\nAufgabe - Summe einer Liste")

# Summe einer Liste: Schreibe eine Funktion, die alle Elemente in einer Liste summiert.
def sum_list(items):
    pass


print("\nAufgabe - Palindrom")

# Palindrom: Erstelle eine Funktion, die überprüft, ob ein Wort ein Palindrom ist: True: level, racecar, radar || False: hello, ship, fish
def is_palindrome(string):
    pass


print(is_palindrome("racecar"))
print(is_palindrome("hello"))


print("\nAufgabe - Spiegeldrucker")
# Spiegeldrucker: Erstelle eine Funktion, die von n herabzählt und anschließend wieder zu n hochzählt:
# 3 -> 3,2,1,2,3
# 5 -> 5,4,3,2,1,2,3,4,5

def mirror_printer(n):
    pass


mirror_printer(3)
mirror_printer(10)


print("\nAufgabe - Höhlenforscher")
# Höhlenforscher: Erstelle eine Funktion, die visualiert, wie eine Figur n-Level hinabsteigt und n-Level wieder hochsteigt. Beachte die Einrückungen.
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
    pass


cave_explorer(3, 1)


print("\nAufgabe - Ziffern zählen")

# Ziffern zählen: Schreibe eine Funktion, die die Ziffern einer Ganzzahl zählt.
def count_digits(n):
    pass

print(count_digits(203))
print(count_digits(53203))


print("\nAufgabe - Summe verschachtelte Liste")

# Schreibe eine Funktion, die alle Zahlen in einer tiefer verschachtelten Liste summiert.
# [1, [2,3, [3,4], 2],12]
def nested_sum(lst):
    pass

print(nested_sum([1, [2, 3, [3, 4], 2], 12]))


print("\nAufgabe- Binary Search")
# Implementiere binary search rekursiv.

def binary_search(arr, low, high, x):
    pass


print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 0, 14, 11))

print("\nAufgabe - Echo")
# Echo: Nehme einen String der Stück für Stück verkleinert wird (jeweils 1. Buchstaben entfernen) und am Ende wieder Stück für Stück zusammengesetzt wird, aber dieses Mal mit Großbuchstaben
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
    pass


echo("hello")
