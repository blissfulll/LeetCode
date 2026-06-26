# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    max_len = 0

    def dfs(self, node, left_len, right_len):

        if not node:
            return

        if self.max_len < left_len:
            self.max_len = left_len
        if self.max_len < right_len:
            self.max_len = right_len

        self.dfs(node.left, right_len+1, 0)
        
        self.dfs(node.right, 0, left_len+1)

    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        self.dfs(root, 0, 0)

        return self.max_len
