class Pet:

    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        self.happiness = 5

    def __str__(self):
        return f"I am instance of the Pet class: name: {self.name} owner: {self.owner} happiness: {self.happiness}"

    def introduce(self):
        print(f"Hi I am {self.name}")

    def bark(self):
        print("Bark!, Bark!")

    def increase_happiness(self, amount):
        if amount > 0:
            self.happiness += amount
        else:
            raise ValueError("amount must be positive")


rex = Pet("rex", "jane")

birdy = Pet("birdy", "john")


# print(rex)
rex.introduce()
birdy.introduce()

print("hello".upper())

print(type("hello"))


birdy.increase_happiness(-10)
print(birdy)


print(isinstance(rex, Pet))
