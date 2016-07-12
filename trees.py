class BinHeap:
    def __init__(self):
        self.heapList = [0]  # 0 element not used
        self.currentSize = 0


    def percUp(self,i):  # perk insert at bottom up
        while i // 2 > 0: # not at top yet
          if self.heapList[i] < self.heapList[i // 2]:
             tmp = self.heapList[i // 2]
             self.heapList[i // 2] = self.heapList[i]
             self.heapList[i] = tmp
          i = i // 2

    def insert(self,k):
      self.heapList.append(k)
      self.currentSize = self.currentSize + 1
      self.percUp(self.currentSize)

    def percDown(self,i): #perk insert at top down
      while (i * 2) <= self.currentSize:
          mc = self.minChild(i)
          if self.heapList[i] > self.heapList[mc]:
              tmp = self.heapList[i]
              self.heapList[i] = self.heapList[mc]
              self.heapList[mc] = tmp
          i = mc

    def minChild(self,i):
      if i * 2 + 1 > self.currentSize: # no right chile
          return i * 2
      else: # return index of smallest of left and right
          if self.heapList[i*2] < self.heapList[i*2+1]:
              return i * 2
          else:
              return i * 2 + 1

    def delMin(self):
      retval = self.heapList[1]
      self.heapList[1] = self.heapList[self.currentSize] # move last to top
      self.currentSize = self.currentSize - 1
      self.heapList.pop() # remove last
      self.percDown(1) # perk new top down
      return retval

    def buildHeap(self,alist):
      i = len(alist) // 2 # do not do any leaf nodes
      self.currentSize = len(alist)
      self.heapList = [0] + alist[:] # create new list with input list
      while (i > 0): # perk bigger down and work up tree
          self.percDown(i)
          i = i - 1

class PriorityQueue(object):

    def __init__(self):
        self.heapList = BinHeap()

    def enqueue(self, item):
        self.heapList.insert((item))

    def dequeue(self):
        return self.heapList.delMin()

import random
for n in [1,2,5,10,20]: # do sequence of each of these lengths
    l1 = [ i+1 for i in range(n)] # list from 1 to n
    l2 = l1.copy() # duplicate the list l1
    random.shuffle(l2) # shuffle it before adding to priority queue pq
    pq = PriorityQueue()
    print("test inserts from: ",l2)
    for i in l2: #add each element from l2
        pq.enqueue(i)
    for i in l1: #check that when dequeued they are lowest to highest [1,2,3...n]
        assert i == pq.dequeue()

print("ALL PASSED")