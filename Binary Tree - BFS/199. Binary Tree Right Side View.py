# https://leetcode.com/problems/binary-tree-right-side-view/description/?envType=study-plan-v2&envId=leetcode-75

class Solution(object):
    # Runtime 15 ms
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def helper(node, depth):
            if node: 
                if depth == len(output):
                    output.append(node.val)
                helper(node.right, depth+1)
                helper(node.left, depth+1)

        output = []
        helper(root, 0)
        return output


    # Runtime 10 ms
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return self.helper(root)
    
    def helper(self, root):
        if root == None:
            return []
        
        left = self.helper(root.left)
        right = self.helper(root.right)
        
        if len(left) <= len(right):
            return [root.val] + right
        else: 
            return [root.val] + right + left[len(right):]


