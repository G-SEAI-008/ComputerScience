class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


stack_one = Stack()

stack_one.push(10)
stack_one.push(20)

print(stack_one.peek())
print(stack_one.pop())
print(stack_one.peek())

print(stack_one.is_empty())
print(stack_one.size())
