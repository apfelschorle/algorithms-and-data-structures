class Stacks:
    def __init__(self):
        self.node = []

    def isEmpty(self):
        return self.node == []

    def peek(self):
        return self.node

    def push(self, node):
        return self.node.append(node)

    def pop(self):
        return self.node.pop()

Stacking = Stacks()
print('Is the stack empty?')
print(Stacking.isEmpty())
print()

print('Adding elements 1, 2, 3, and 4...')
Stacking.push(1)
Stacking.push(2)
Stacking.push(3)
Stacking.push(4)
print('... done.')
print()

print('Is the stack empty?')
print(Stacking.isEmpty())
print()

print('What is the stack now?')
print(Stacking.peek())

print('Removing an element (LIFO)...')
Stacking.pop()
print('... done.')
print()

print('What is the stack now?')
print(Stacking.peek())
