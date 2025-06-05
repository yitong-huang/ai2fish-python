class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()


queue = Queue()
queue.enqueue(5)
queue.enqueue(20)
print(queue.dequeue())
queue.enqueue(10)
print(queue.dequeue())
print(queue.dequeue())

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        self.items.pop(0)
