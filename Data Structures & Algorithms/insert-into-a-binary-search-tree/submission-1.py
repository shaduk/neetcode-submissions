# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def helper(root, val):
            if root == None:
                return
            if val > root.val:
                right = helper(root.right, val)
                if right == None:
                    root.right = TreeNode(val)
            else:
                left = helper(root.left, val)
                if left == None:
                    root.left = TreeNode(val)
            return root
        if root == None:
            return TreeNode(val)
        
        return helper(root, val)