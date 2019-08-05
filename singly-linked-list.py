class listNode(object):
    def __init__(self, data, node = None):
        self.data = data
        self.next_node = node

    def get_next(self):
        return self.next_node

    def set_next(self, node):
        self.next_node = node

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

class LinkedList(object):
    def __init__(self, root = None):
        self.root = root
        self.size = 0

    def get_size(self):
        return self.size

    def add(self, data):
        new_node = listNode(data, self.root)
        self.root = new_node
        self.size += 1

    def remove(self, data):
        this_node = self.root
        prev_node = None
        while this_node:
            if this_node.get_data() == data:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node.get_next()
                self.size -= 1
                return True
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False

    def findIndex(self, data):
        this_node = self.root
        counter = 0
        while this_node:
            if this_node.get_data() == data:
                return counter
            this_node = this_node.get_next()
            counter += 1
        return None

    def traverse(self):
        temp = self.root
        while(temp):
            print('{0} '.format(temp.data), end='')
            temp = temp.get_next()

    def reverse(self):
        previous = None
        current = self.root
        while(current is not None):
            next_node = current.get_next()
            current.next_node = previous
            previous = current
            current = next_node
        self.root = previous

myList = LinkedList()
myList.add(5)
myList.add(8)
myList.add(12)
myList.traverse()
print()
print(myList.findIndex(12))
myList.reverse()
print(myList.traverse())
print(myList.findIndex(12))
myList.remove(8)
print(myList.traverse())
print(myList.remove(12))
print(myList.remove(13))
