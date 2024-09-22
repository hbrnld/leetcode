# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/?envType=study-plan-v2&envId=leetcode-75

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict

class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        levels = defaultdict(int)

        def sum_values(root, depth):
            if root: 
                levels[depth] += root.val
                sum_values(root.left, depth+1)
                sum_values(root.right, depth+1)

        sum_values(root, 1)

        return max(levels, key=levels.get)