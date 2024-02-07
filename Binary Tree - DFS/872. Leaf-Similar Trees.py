# https://leetcode.com/problems/leaf-similar-trees/?envType=study-plan-v2&envId=leetcode-75

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        return self.findLeafNodes(root1) == self.findLeafNodes(root2)
    
    def findLeafNodes(self, root):
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        return self.findLeafNodes(root.left) + self.findLeafNodes(root.right)