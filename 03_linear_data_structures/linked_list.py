class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, value):
        node = Node(value)
        self.length += 1
        if not self.head:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node

    def addFirst(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        self.length += 1

    def _find(self, index):
        if index >= self.length:
            return None
        current = self.head
        for i in range(index):
            current = current.next
        return current

    def insertAt(self, index, value):
        if index == self.length - 1:
            self.push(value)
        elif index == 0:
            self.addFirst(value)
        else:
            new_node = Node(value)
            node = self._find(index - 1)
            new_node.next = node.next
            node.next = new_node
            self.length += 1

    def printList(self):
        node = self.head
        while node:
            print(node.value)
            node = node.next

    def delete(self, index):
        if index == 0:
            head = self.head
            if head:
                self.head = head.next
            else:
                self.head = None
                self.tail = None
            self.length -= 1
            return head.value

        node = self._find(index - 1)
        excise = node.next
        if not excise:
            return None
        node.next = excise.next
        if not node.next:
            self.tail = node
        self.length -= 1
        return excise.value


my_linked_list = LinkedList()


my_linked_list.push("A")
my_linked_list.push("B")
my_linked_list.push("C")
my_linked_list.push("D")

my_linked_list.insertAt(2, "K")
my_linked_list.insertAt(0, "AA")
my_linked_list.insertAt(6, "ZZ")
my_linked_list.delete(3)
my_linked_list.delete(0)
my_linked_list.delete(4)

my_linked_list.printList()
