# https://leetcode.com/problems/maximum-subsequence-score/description/?envType=study-plan-v2&envId=leetcode-75

import heapq

nums1 = [1,3,3,2]
nums2 = [2,1,3,4]

class Solution(object):
    def maxScore(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """

        curMax = 0
        prefixSum = 0
        minHeap = []

        # Sort zipped lists in descending order of nums2
        for a, b in sorted(list(zip(nums1, nums2)), key=lambda x: x[1], reverse=True):
            #print(a, b)
            prefixSum += a
            heapq.heappush(minHeap, a)

            if len(minHeap) == k:
                curMax = max(curMax, prefixSum * b)
                prefixSum -= heapq.heappop(minHeap)
                #print(f"b is {b}, prefixSum is {prefixSum}, curMax is {curMax}")

        return curMax