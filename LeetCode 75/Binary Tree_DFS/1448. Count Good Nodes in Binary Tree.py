# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    counter = 0

    def dfs(self, node, max_val):
        # print(node.val, max_val)
        
        if node.val > max_val:
            max_val = node.val
        
        if max_val <= node.val:
            self.counter += 1
            # print(node.val, "COUNT")

        if node.left:
            # print(node.val, "LEFT")
            self.dfs(node.left, max_val)

        if node.right:
            # print(node.val, "RIGHT")
            self.dfs(node.right, max_val)
    
    def goodNodes(self, root: TreeNode) -> int:
        
        max_val = root.val

        self.dfs(root, max_val)

        return self.counter
