# https://leetcode.com/problems/path-sum-iii/description/?envType=study-plan-v2&envId=leetcode-75

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict

class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
    
        def dfs(root, curSum):
            count = 0
            if root:
                # Update current sum
                curSum += root.val
                
                # Get count of missing until target
                count = prefixSums[curSum-targetSum]

                # Add value of this prefixSum
                prefixSums[curSum] += 1

                # Explore children
                count += dfs(root.left, curSum) + dfs(root.right, curSum)
                
                # Remove value of this prefixSum (path's been explored)
                prefixSums[curSum] -= 1

            return count

        # Keep track of prefix sums {prefixSum: count}
        prefixSums = defaultdict(int)
        prefixSums[0] = 1

        return dfs(root, 0)
