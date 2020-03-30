from heapq import heappush

class binaryHeapMin:

    def __init__(self):
        self.heap = []

    def push(self, i):
        heappush(self.heap, i)

##    def pop(self):
##        heappop(self.heap)

    def returnHeap(self):
        return self.heap

heap = binaryHeapMin()
startingList = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
print(startingList)

for item in startingList:
    heap.push(item)
print(heap.returnHeap())

##heap.pop(9)
##print(heap.returnHeap())
