# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        node_queue = []
        level = 0

        def bfsRec(node, level, res):
            
            if hasattr(node, "left"):
                if len(res) == level:
                    res.append([])
                res[level].append(node.val)
                bfsRec(node.left, level + 1, res)

            if hasattr(node, "right"):
                if len(res) == level:
                    res.append([])
                res[level].append(node.val)
                bfsRec(node.right, level + 1, res)

            return

        bfsRec(root, level, node_queue)

        res = []
        for arr in node_queue:
            res.append(arr[-1])

        return res
        
