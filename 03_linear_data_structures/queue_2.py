from linked_list import LinkedList


class Queue:

    def __init__(self):
        self.queue = LinkedList()

    def enqueue(self, item):
        self.queue.push(item)

    def dequeue(self):
        self.queue.delete(0)

    def peek(self):
        return self.queue.head

    def isEmpty(self):
        return self.queue.length == 0

    def printQueue(self):
        self.queue.printList()
