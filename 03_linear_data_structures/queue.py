from collections import deque


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue.pop(0)

    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue[0]

    def isEmpty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


myQueue = Queue()

myQueue.enqueue("A")
myQueue.enqueue("B")
myQueue.enqueue("C")

print(myQueue.queue)

print(myQueue.size())

print(myQueue.dequeue())
print(myQueue.peek())
