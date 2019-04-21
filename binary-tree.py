class treeNode:
    def __init__(self, val):
        self.leftNode = None
        self.rightNode = None
        self.val = val

    def insert(self, val):
        if self.val:
            if val < self.val:
                if self.leftNode is None:
                    self.leftNode = treeNode(val)
                else:
                    self.leftNode.insert(val)
            else:
                if self.rightNode is None:
                    self.rightNode = treeNode(val)
                else:
                    self.rightNode.insert(val)
        else:
            self.val = val

    def find(self, findval):
        if findval < self.val:
            if self.leftNode is None:
                return False
            return self.leftNode.find(findval)
        elif findval > self.val:
            if self.rightNode is None:
                return False
            return self.rightNode.find(findval)
        else:
            return True

    def PrintTree(self):
        ## pre-order
        #print(self.val),
        if self.leftNode:
            self.leftNode.PrintTree()

        ## in-order
        print(self.val),
        if self.rightNode:
            self.rightNode.PrintTree()

        ## post-order
        #print(self.val),

####
root = treeNode(8)
root.insert(6)
root.insert(7)
root.insert(5)
root.insert(3)
root.insert(0)
root.insert(9)
####
root.PrintTree()
print(root.find(9))
print(root.find(10))
