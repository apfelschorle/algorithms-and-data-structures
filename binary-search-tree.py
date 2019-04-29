class treeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val),
            self.inorder(root.right)

    def insert(self, node, val):
        if node:    
            if val < node.val:
                node.left = self.insert(node.left, val)
            else:
                node.right = self.insert(node.right, val)
        else:
            return treeNode(val)
        return node

    def minValueNode(self, node): 
        current = node 
        while(current.left is not None): 
            current = current.left  
      
        return current  

    def deleteNode(self, root, val): 
        if root:
            if val < root.val: 
                root.left = self.deleteNode(root.left, val) 
            elif(val > root.val): 
                root.right = self.deleteNode(root.right, val) 
            else: 
                  
                if root.left is None: 
                    temp = root.right  
                    root = None 
                    return temp  
                      
                if root.right is None: 
                    temp = root.left  
                    root = None
                    return temp 
          
                temp = self.minValueNode(root.right) 
                root.val = temp.val 
                root.right = self.deleteNode(root.right, temp.val)
        else:
            return root
      
        return root

####
root = treeNode(8)
root = root.insert(root, 6)
root = root.insert(root, 7)
root = root.insert(root, 5)
root = root.insert(root, 3)
root = root.insert(root, 0)
root = root.insert(root, 9)
####
root.inorder(root) 
  
print("\nDelete 6")
root = root.deleteNode(root, 6)
root.inorder(root) 
  
print("\nDelete 3")
root = root.deleteNode(root, 3)
root.inorder(root) 
  
print("\nDelete 9")
root = root.deleteNode(root, 9)
root.inorder(root)
