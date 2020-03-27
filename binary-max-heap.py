class maxHeap:
    def __init__(self, items = []):
        ##super().__init__()
        self.heap = [0]
        for i in items:
            self.heap.append(i)
            self.__floatUp(len(self.heap) - 1)

    def push(self, data):
        self.heap.append(data)
        self.__floatUp(len(self.heap) - 1)

    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return False

    def pop(self):
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap) - 1)
            max = self.heap.pop()
            self.__bubbleDown(1)
        elif len(self.heap) == 2:
            max = self.heap.pop()
        else:
            max = False
        return max

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __floatUp(self, index):
        parent = index//2
        if index <= 1:
            return
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            self.__floatUp(parent)

    def __bubbleDown(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self.__swap(index, largest)
            self.__bubbleDown(largest)

m = maxHeap([95, 3, 21])
m.push(10)
print(str(m.heap[1:len(m.heap)]))

##from heapq import heappush, heappop, heapify  
##
##class MinHeap: 
##
##    def __init__(self): 
##        self.heap = []  
##  
##    def parent(self, i): 
##        return (i-1)/2
##      
##    def insertKey(self, k): 
##        heappush(self.heap, k)            
##  
##    def decreaseKey(self, i, new_val): 
##        self.heap[i]  = new_val  
##        while(i != 0 and self.heap[self.parent(i)] > self.heap[i]): 
##            # Swap heap[i] with heap[parent(i)] 
##            self.heap[i] , self.heap[self.parent(i)] = ( 
##            self.heap[self.parent(i)], self.heap[i]) 
##              
##    def extractMin(self): 
##        return heappop(self.heap) 
##  
##    def deleteKey(self, i): 
##        self.decreaseKey(i, float("-inf")) 
##        self.extractMin() 
##  
##    def getMin(self): 
##        return self.heap[0] 
##  
##heapObj = MinHeap() 
##heapObj.insertKey(3) 
##heapObj.insertKey(2) 
##heapObj.deleteKey(1) 
##heapObj.insertKey(15) 
##heapObj.insertKey(5) 
##heapObj.insertKey(4) 
##heapObj.insertKey(45) 
##  
##print heapObj.extractMin(), 
##print heapObj.getMin(), 
##heapObj.decreaseKey(2, 1) 
##print heapObj.getMin() 
