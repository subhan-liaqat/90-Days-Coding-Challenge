# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.d=defaultdict(list)
        def foo(x,depth):
            self.d[depth].append(x.val)
            if x.left: foo(x.left,depth+1)
            if x.right: foo(x.right,depth+1)
        if root: foo(root,0)
        return [self.d[i] for i in sorted(self.d.keys())]