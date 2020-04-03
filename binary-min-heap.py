from heapq import heappush, heappop

class binaryHeapMin:

    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1)/2

    def push(self, j):
        heappush(self.heap, j)

    def pop(self):
        heappop(self.heap)

    def decrease(self, i, val):
        self.heap[i] = val
        while(i != 0 and self.heap[self.parent(i)] > self.heap[i]):
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]

    def delete(self, i):
        self.decrease(i)
        self.pop()

    def returnHeap(self):
        return self.heap

heap = binaryHeapMin()
startingList = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]

print('This is the starting list:')
print(startingList)
print()

print('This is the list when it has been heapified.')
for item in startingList:
    heap.push(item)
print(heap.returnHeap())
print()

print('This is the list when it has been re-heapified when the smallest element has been removed.')
heap.pop()
print(heap.returnHeap())
