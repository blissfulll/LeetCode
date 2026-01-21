# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        path_sum = [root.val]
        res = [0]

        def dfsRec(root, path_sum, res):

            print(path_sum)

            node_l, node_r = None, None
            
            if hasattr(root, "left"):
                node_l = root.left
                for val in path_sum:
                    tmp_sum = node_l.val + val
                    path_sum.append(tmp_sum)
                    if tmp_sum == targetSum:
                        res[0] += 1
                path_sum.append(node_l.val)
                dfsRec(node_l, path_sum, res)

            if hasattr(root, "left"):
                node_r = root.right
                for val in path_sum:
                    tmp_sum = node_r.val + val
                    path_sum.append(tmp_sum)
                    if tmp_sum == targetSum:
                        res[0] += 1
                path_sum.append(node_r.val)
                dfsRec(node_r, path_sum, res)    
            
            return

        dfsRec(root, path_sum, res)

        return res[0]
