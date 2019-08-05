class listNode(object):
    def __init__(self, data, node = None):
        self.data = data
        self.next = node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, node):
        self.next = node

class LinkedList(object):
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = listNode(data, self.head)
        self.head = new_node

    def remove(self, data):
        this_node = self.head
        prev_node = None
        while this_node:
            if this_node.get_data() == data:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.head = this_node.get_next()
                return True
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False

    def getIndex(self, data):
        this_node = self.head
        counter = 0
        while this_node:
            if this_node.get_data() == data:
                return counter
            this_node = this_node.get_next()
            counter += 1
        return None

    def traverse(self):
        temp = self.head
        while(temp):
            print('{0} '.format(temp.data), end='')
            temp = temp.get_next()

    def reverse(self):
        previous = None
        current = self.head
        while(current is not None):
            next_node = current.get_next()
            current.next_node = previous
            previous = current
            current = next_node      
        self.head = previous
        if current is not None:
            print('{0} '.format(current), end='')

if __name__ == '__main__':
    ## Initialisation
    singlyLinkedList = LinkedList()

    ## Insert
    singlyLinkedList.insert(5)
    singlyLinkedList.insert(8)
    singlyLinkedList.insert(12)

    ## First traverse
    print('-- Traversal')
    singlyLinkedList.traverse()
    print()

    ## First indexing
    print('-- Where is the index of the integer 12 in the list?')
    print(singlyLinkedList.getIndex(12))

    ## Reversal and second traverse
    print('-- Reversal')
    singlyLinkedList.reverse()
    singlyLinkedList.traverse()
    print()

    ## Second indexing
    print('-- Where is the index of the integer 12 in the list now?')
    print(singlyLinkedList.getIndex(12))

    ## Removal from the list
    print('-- Removing 8 from the list')
    singlyLinkedList.remove(8)
    singlyLinkedList.traverse()
    print()

    ## Removal indicator
    print('-- 12 is removed from the list?')
    print(singlyLinkedList.remove(12))
    print('-- 13 is removed from the list?')
    print(singlyLinkedList.remove(13))
