# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, r, s):
        def match(a, b):
            if not a and not b: return True
            if a and b and a.val == b.val:
                return match(a.left, b.left) and match(a.right, b.right)
            return False

        if not s: return True
        if not r: return False
        return match(r, s) or self.isSubtree(r.left, s) or self.isSubtree(r.right, s)
