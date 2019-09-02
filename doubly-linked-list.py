class listNode(object):
    def __init__(self, data, next_node = None, prev_node = None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node

    def get_next(self):
        return self.next_node

    def set_next(self, next_node):
        self.next_node = next_node

    def get_prev(self):
        return self.prev_node

    def set_prev(self, prev_node):
        self.prev_node = prev_node

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

class LinkedList(object):
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = listNode(data, self.head)
        if self.head:
            self.head.set_prev(new_node)
        self.head = new_node

    def remove(self, data):
        this_node = self.head
        while this_node:
            if this_node.get_data() == data:
                next_node = this_node.get_next()
                prev_node = this_node.get_prev()          
                if next_node:
                    next_node.set_prev(prev_node)
                if prev_node:
                    prev_node.set_next(next_node)
                else:
                    self.head = this_node
                return True
            else:
                this_node = this_node.get_next()
        return False

    def getIndex(self, data):
        this_node = self.head
        counter = 0
        while this_node:
            if this_node.get_data() == data:
                return counter
            else:
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
            current.prev_node = next_node
            previous = current
            current = next_node
        self.head = previous
        if current is not None:
            print('{0} '.format(current), end='')

if __name__ == '__main__':
    ## Initialisation
    doublyLinkedList = LinkedList()

    ## Insert
    doublyLinkedList.insert(5)
    doublyLinkedList.insert(8)
    doublyLinkedList.insert(12)

    ## First traverse
    print('-- Traversal')
    doublyLinkedList.traverse()
    print()

    ## First indexing
    print('-- Where is the index of the integer 12 in the list?')
    print(doublyLinkedList.getIndex(12))

    ## Reversal and second traverse
    print('-- Reversal')
    doublyLinkedList.reverse()
    doublyLinkedList.traverse()
    print()

    ## Second indexing
    print('-- Where is the index of the integer 12 in the list now?')
    print(doublyLinkedList.getIndex(12))

    ## Removal from the list
    print('-- Removing 8 from the list')
    doublyLinkedList.remove(8)
    doublyLinkedList.traverse()
    print()

    ## Removal indicator
    print('-- 12 is removed from the list?')
    print(doublyLinkedList.remove(12))
    print('-- 13 is removed from the list?')
    print(doublyLinkedList.remove(13))
