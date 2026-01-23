# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def check_compat(node, side):
            if hasattr(node, side):
                return false
            return True

        
        def get_new_node(node):
            if hasattr(node, "left"):
                if hasattr(node, "right"):
                    if check_compat(node.left, "right"):
                        node.left.right = node.right
                        return node.left 
                    elif check_compat(node.right, "left"):
                        node.right.left = node.left
                        return node.right
                else:
                    return node.left

                return node.left
            return None

        def dfsRec(node):

            if key < node.val:
                if hasattr(node, "left"):
                    if node.left.val == key:
                        node.left = get_new_node(node.left)
                        return
                    else:
                        dfsRec(node.left)

            elif key > node.val:

                if hasattr(node, "right"):
                    if node.right.val == key:
                        node.right = get_new_node(node.right)
                        return
                    else:
                        dfsRec(node.right)
            else:
                return


        if root.val == key:
            root = get_new_node(root)
        else:
            dfsRec(root)
        
        return root
