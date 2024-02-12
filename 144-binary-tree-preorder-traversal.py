# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        result = []

        def preorder(root) :
            if not root:
                return
            else:
                result.append(root.val)
                preorder(root.left)
                preorder(root.right)
        preorder(root)
        return result
