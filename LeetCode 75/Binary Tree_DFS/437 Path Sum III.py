# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        path_sum = []
        res = [0]

        def dfsRec(root, path_sum, res):

            if not root:
                return

            # pop_count = 0
            tmp_path_sum = []
            for val in path_sum:
                tmp_sum = root.val + val
                tmp_path_sum.append(tmp_sum)
                if tmp_sum == targetSum:
                    res[0] += 1
                # pop_count += 1
            tmp_path_sum.append(root.val)
            if root.val == targetSum:
                res[0] += 1
            path_sum = tmp_path_sum
            # print(path_sum)

            # print(path_sum)
            # c_1 = path_sum.copy()

            if hasattr(root, "left"):
                node_l = root.left
                dfsRec(node_l, path_sum, res)

            # # c_2 = path_sum.copy()
            
            if hasattr(root, "right"):
                node_r = root.right
                # for i in range(pop_count):
                #     path_sum.pop()
                dfsRec(node_r, path_sum, res)
            
            return

        dfsRec(root, path_sum, res)

        return res[0]
