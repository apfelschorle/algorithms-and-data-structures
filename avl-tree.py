class treeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
        self.height = 1

class AVL_tree(object):
    def insert(self, node, val):
        if node:    
            if val < node.val:
                node.left = self.insert(node.left, val)
            else:
                node.right = self.insert(node.right, val)
        else:
            return treeNode(val)

        node.height = 1 + max(self.treeHeight(node.left), self.treeHeight(node.right))
        balance = self.treeBalance(node)

        if balance > 1: ## Left case
            if val < node.left.val: ## Left-left
                return self.rightRotate(node)
            else: ## Left-right
                node.left = self.leftRotate(node.left) 
                return self.rightRotate(node) 

        if balance < -1: ## Right case
            if val < node.right.val: ## Right-left
                node.right = self.rightRotate(node.right) 
                return self.leftRotate(node) 
            else: ## Right-right
                return self.leftRotate(node)      
        return node

    def delete(self, root, val): 
        if root or root is not None:
            if val < root.val: 
                root.left = self.delete(root.left, val) 
            elif val > root.val: 
                root.right = self.delete(root.right, val) 
            else: 
                  
                if root.left is None: 
                    temp = root.right  
                    root = None 
                    return temp  
                      
                if root.right is None: 
                    temp = root.left  
                    root = None
                    return temp 
          
                temp = self.min(root.right) 
                root.val = temp.val 
                root.right = self.delete(root.right, temp.val)
        else:
            return root

        root.height = 1 + max(self.treeHeight(root.left), self.treeHeight(root.right))
        balance = self.treeBalance(root)

        if balance > 1: ## Left case
            if self.treeBalance(root.left) > -1: ## Left-left
                return self.rightRotate(root)
            else: ## Left-right
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
            
        if balance < -1: ## Right case
            if self.treeBalance(root.right) < 1: ## Right-left
                return self.leftRotate(root)
            else: ## Right-right
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
           
        return root

    def leftRotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.treeHeight(z.left), self.treeHeight(z.right))
        y.height = 1 + max(self.treeHeight(y.left), self.treeHeight(y.right))

        return y
    
    def rightRotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.treeHeight(z.left), self.treeHeight(z.right))
        y.height = 1 + max(self.treeHeight(y.left), self.treeHeight(y.right))

        return y

    def treeHeight(self, node):
        if not node:
            return 0
        return node.height

    def treeBalance(self, node):
        if not node:
            return 0
        return self.treeHeight(node.left) - self.treeHeight(node.right)

    def min(self, root):
        if root is None or root.left is None: 
            return root 
        return self.min(root.left) 

    def preOrder_sort(self, root):
        if root:
            print("{0} ".format(root.val), end="")
            self.preOrder_sort(root.left)
            self.preOrder_sort(root.right)

    def inOrder_sort(self, root):
        if root:
            self.inOrder_sort(root.left)
            print("{0} ".format(root.val), end="")
            self.inOrder_sort(root.right)

    def postOrder_sort(self, root):
        if root:
            self.postOrder_sort(root.left)
            self.postOrder_sort(root.right)
            print("{0} ".format(root.val), end="")

####
tree = AVL_tree()
root = None

root = tree.insert(root, 10)
root = tree.insert(root, 20)
root = tree.insert(root, 30)
root = tree.insert(root, 40)
root = tree.insert(root, 50)
root = tree.insert(root, 25)
####
print('Pre-order sorting')
tree.preOrder_sort(root)
print()
print('In-order sorting:')
tree.inOrder_sort(root)
print()
print('Post-order sorting:')
tree.postOrder_sort(root)
print()
###
root = tree.delete(root, 30)

print('Pre-order sorting')
tree.preOrder_sort(root)
print()
print('In-order sorting:')
tree.inOrder_sort(root)
print()
print('Post-order sorting:')
tree.postOrder_sort(root)
print()
