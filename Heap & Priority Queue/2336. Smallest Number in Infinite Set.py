# https://leetcode.com/problems/smallest-number-in-infinite-set/?envType=study-plan-v2&envId=leetcode-75

import heapq

class SmallestInfiniteSet(object):
    def __init__(self):
        self.heap=[]
        self.largest=1

    def popSmallest(self):
        if self.heap:
            smallest = heapq.heappop(self.heap)
            return smallest
        
        n = self.largest
        self.largest += 1
        return n
    
    def addBack(self, num):
        if num < self.largest and num not in self.heap:
            heapq.heappush(self.heap, num)