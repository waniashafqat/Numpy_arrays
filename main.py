import numpy as np
class Queue:
    # Special method to initialize attributes.
    def __init__(self):
        self.array = np.arange(10)

    def display(self):
        return self.array

    def is_empty(self):
        return (len(self.array) == 0)

    def enqueue(self, data):
        x = np.append(self.array, data)
        return x

    def dequeue(self):
        self.array = np.delete(self.array, 0)

    def rear(self):
        return self.array(-1)

    def front(self):
        return self.array(0)

    def size(self):
        return (len(self.array) > 10)


# Initializing queue.
q = Queue()
q.enqueue(1)
q.enqueue(5)
q.enqueue(10)
