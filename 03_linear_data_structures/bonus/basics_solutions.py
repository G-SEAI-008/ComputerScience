# Regeln:
# Kein "händisches" Zählen der Indexpositionen erlaubt
# Keine Künstliche Intelligenz

# String
text = "My Python is better than your Python"

print("\nAufgabe 1")
# Finde den Index des Buchtabens "b"
print(text.index("b"))

print("\nAufgabe 2")
# Erstelle einen Substring aus dem Wort "better".
better_start_index = text.index("better")
better = text[better_start_index : better_start_index + len("better")]
print(better)

print("\nAufgabe 3")
# Ändere alle "t"s zu "f"
text = text.replace("t", "f")
print(text)

print("\nAufgabe 4")
# Ändere den Datentyp des Textes in eine Liste
text = text.split()
print(text)

print("\nAufgabe 5")
# Mach aus der Liste wieder einen String
text = " ".join(text)
print(type(text))

print("\nAufgabe 6")
# Tausche die Position der beiden Buchstaben in dem Wort "is"
text_list = list(text)
is_index = text.index("is")
text_list[is_index], text_list[is_index + 1] = (
    text_list[is_index + 1],
    text_list[is_index],
)
text = "".join(text_list)
print(text)

print("\nAufgabe 7")
# Ändere jeden Anfangbuchstaben eines Wortes zu einem Großbuchstaben
text = " ".join([word.capitalize() for word in text.split()])
print(text)
# text.title()

print("\nAufgabe 8")
# Aufabe 5:
# Entferne alle Vokale aus dem text

text = "".join([char for char in text if char not in "aeiouAEIOU"])
print(text)

print("\nAufgabe 9")
# Aufabe 5:
email = "karl@example.org"
# Filtere die Domain heraus und weise sie einer neuen Variable zu.
domain = email.split("@")[1].split(".")[0]
print(domain)


print("\nAufgabe 10")
# \nAufgabe 10:
# Rotiere das Wort python thonpy.
rotated = "python"[2:] + "python"[:2]
print(rotated)


print("\nAufgabe 11")
# \nAufgabe :
# Erstelle eine Akronym aus den Anfangsbuchstaben jedes Wortes.
text_two = "You Only Live Once"
print("".join([word[0] for word in text_two.split()]))

print("\nAufgabe 12")
my_url = "http://www.example.org"
# Überprüfe, ob die Url mit "http://" beginnt.
print(my_url.startswith("http://"))


print("\nAufgabe 13")
# Filtere die Zahl heraus und wandle sie in ein float um.
price = "The total is 45.99€"
clean_price = float("".join(char for char in price if char.isdigit() or char == "."))
print(clean_price)


# Lists
colours = ["red", "green", "blue", "yellow"]

print("\nAufgabe 14")
# Ändere "blue" zu "cyan"
# colours[colours.index("blue")] = "cyan"
colours = ["cyan" if colour == "blue" else colour for colour in colours]
print(colours)

print("\nAufgabe 15")
# Tausche das erste Element mit dem letzten Element
colours[0], colours[-1] = colours[-1], colours[0]
print(colours)

print("\nAufgabe 16")
# Füge "magenta" ans Ende hinzu
colours.append("magenta")
print(colours)

print("\nAufgabe 17")
# Check ob "green" in der Liste ist
print("green" in colours)


print("\nAufgabe 18")
# Entferne "green" aus der Liste.
colours = [colour for colour in colours if colour != "green"]
print(colours)

print("\nAufgabe 19")
# Erstelle eine neue Liste mit den letzten drei Element aus "colours" in umgekehrte Reihenfolge
colour_part = colours[-1:-4:-1]
print(colour_part)


person = {"firstname": "karl", "lastname": "karlsen", "age": 30}

print("\nAufgabe 20")
# Füge einen neuen Key hinzu
person["location"] = "berlin"
print(person)

print("\nAufgabe 21")
# Überprüfe, ob "age" als key existiert
print("age" in person)


print("\nAufgabe 22")
string_one = "abrakadabra"
# Nutze ein Dictionary um die Häufigkeit jedes einzelnen Buchstaben innerhalb "string_one" zu ermitteln.

counter = {}
for char in string_one:
    if char not in counter:
        counter[char] = 1
    else:
        counter[char] += 1

print(counter)


# my_dict = dict()
# for c in string_one:
#     my_dict[c] = my_dict.get(c, 0) + 1
# print(my_dict)


print("\nAufgabe 23")
# Nimm die folgende Listen und baue daraus ein Dictionary. Die Element aus first_list sind die keys und die Elemente aus second_list die values.
first_list = [1, 2, 3]
second_list = ["A", "B", "C"]

print(dict(zip(first_list, second_list)))


print("\nAufgabe 24")
# Schreibe eine Funktion, die uns den Pfad innerhalb dieses Dateisystems zum Ordner "python" wiedergibt.
# home/user/desktop/solutions/python

file_system = {
    "home": {
        "user": {
            "projects": [""],
            "desktop": {
                "private": {"pictures": ["a.jpg", "b.jpg", "c.jpg"]},
                "job": {"tasks": ["task_a", "task_b"]},
                "solutions": {"python": ["two_sum"]},
            },
        }
    }
}


def find_path(fs, target, current_path=""):
    for key, value in fs.items():
        new_path = f"{current_path}/{key}" if current_path else key
        if key == target:
            return new_path

    if isinstance(value, dict):
        result = find_path(value, target, new_path)
        if result:
            return result
    return None


print(find_path(file_system, "python"))
