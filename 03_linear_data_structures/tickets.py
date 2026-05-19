from collections import deque


def timeRequiredToBuy(tickets, k):
    queue = deque()

    for i in range(len(tickets)):
        queue.append(i)

    time = 0

    while queue:
        time += 1
        front = queue.popleft()
        tickets[front] -= 1

        if k == front and tickets[front] == 0:
            return time

        if tickets[front] != 0:
            queue.append(front)
    return time


print(timeRequiredToBuy([2, 3, 2], 2))


def timeRequiredToBuyB(tickets, k):
    time = 0

    for i in range(len(tickets)):
        if i <= k:
            time += min(tickets[k], tickets[i])
        else:
            time += min(tickets[k] - 1, tickets[i])
    return time


print(timeRequiredToBuyB([2, 3, 2, 4], 2))


def timeRequiredToBuyC(tickets: list, k: int):
    time = 0
    while tickets[k] > 0:
        for person, amount in enumerate(tickets):
            if amount > 0 and tickets[k] != 0:
                tickets[person] -= 1
                time += 1
    return time


print(timeRequiredToBuyC([2, 3, 2, 4], 2))
print(timeRequiredToBuyC([2, 3, 2], 2))
