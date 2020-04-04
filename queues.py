class Queues:
    def __init__(self):
        self.node = []

    def isEmpty(self):
        return self.node == []

    def peek(self):
        return self.node

    def enqueue(self, node):
        return self.node.append(node)

    def dequeue(self):
        return self.node.pop(0)

Queuing = Queues()
print('Is the stack empty?')
print(Queuing.isEmpty())
print()

print('Adding elements 1, 2, 3, and 4...')
Queuing.enqueue(1)
Queuing.enqueue(2)
Queuing.enqueue(3)
Queuing.enqueue(4)
print('... done.')
print()

print('Is the stack empty?')
print(Queuing.isEmpty())
print()

print('What is the stack now?')
print(Queuing.peek())

print('Removing an element... (FIFO)')
Queuing.dequeue()
print('... done.')
print()

print('What is the stack now?')
print(Queuing.peek())
