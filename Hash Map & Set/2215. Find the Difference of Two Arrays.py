# https://leetcode.com/problems/find-the-difference-of-two-arrays/description/?envType=study-plan-v2&envId=leetcode-75

class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        a1 = []
        a2 = []
        nums1, nums2 = set(nums1), set(nums2)

        for num in nums1:
            if num not in nums2:
                a1.append(num) 
        for num in nums2: 
            if num not in nums1:
                a2.append(num)

        return [a1, a2]

        # Another, more compact solution:   
        # return [list(nums1-nums2), list(nums2-nums1)]


            