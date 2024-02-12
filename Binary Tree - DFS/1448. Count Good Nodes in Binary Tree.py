# https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/?envType=study-plan-v2&envId=leetcode-75

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Recursive function to traverse the tree (depth-first search)
        def dfs(root, mx):
            if not root: 
                return
            
            if root.val >= mx: 
                good[0] += 1
                mx = root.val
            
            dfs(root.left, mx)
            dfs(root.right, mx)

        # Wrapped in a list due to the nature of Python's pass-by-object-reference 
        # (integer is immutable, so it's not passed by reference)
        good = [0]      
        dfs(root, -1e4)
        
        return good[0]

        