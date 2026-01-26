# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        # def type1_del(node, parent_node, side):
        #     setattr(parent_node, side, None)

        # def type2_del(node, parent_node, side, parent_side):
        #     setattr(parent_node, parent_side, getattr(node, side))

        # def node_del(node, parent_node, del_node, root_node):
        def node_del(root_node, side, del_node, parent_node, node):

            # if not node:
            #     return

            # print("AAAAAA")
            # if not node:
            #     # print(parent_node.val, "BBBBB")
                
            #     root_node.left = parent_node
            #     parent_node.right = getattr(node, "left", None)
            #     return
           
            if hasattr(node, "right") and node.right != None:
                node_del(root_node, side, del_node, node, node.right)
            else:
                # print(parent_node.val, root_node.val, del_node.val, node.val)
                if root_node == del_node == parent_node:
                    root_node.val = node.val

                    root_node.left = getattr(node, "left", None)
                    return 

                if root_node == del_node:
                    # print("AAAAAA", node.val, root_node.right.val, root_node.left.val, parent_node.val)
                    parent_node.right = getattr(node, "left", None)
                    setattr(node, "right", root_node.right)
                    setattr(node, "left", root_node.left)
                    root_node.val = node.val
                    root_node = node
                    return

                if parent_node == del_node:
                    # print(parent_node.val)
                    setattr(node, "right", del_node.right)
                    setattr(root_node, side, node)
                    # print(parent_node.val)
                    return

                # print(node.val, parent_node.val, del_node.val, root_node.val)
                parent_node.right = getattr(node, "left", None)
                
                node.right = getattr(del_node, "right")
                node.left = del_node.left 
                # if root_node == del_node:
                #     print(node.val)
                #     root_node = node
                del_node.val = node.val
                # del_node = node

                

                # root_node.left = node
                # # if del_node.left != node else None
                
                # parent_node.right = getattr(node, "left", None)
                
        def check_del_type(node, parent_node, side):
            if getattr(node, "right") != None and getattr(node, "left") != None:
                # print(node.val, "FFFFF", parent_node.val)
                # node_del(node.left, node, node, parent_node)
                # print("AAAAAAA")
                node_del(parent_node, side, node, node, node.left)
            elif getattr(node, "right"):
                # type2_del(node, parent_node, "right", side)
                # print(parent_node.val, node.val)
                setattr(parent_node, side, node.right)
            elif getattr(node, "left"):
                # type2_del(node, parent_node, "left", side)
                setattr(parent_node, side, node.left)
            else:
                # type1_del(node, parent_node, side)
                setattr(parent_node, side, None)

        def tree_traversal(node, key, parent_node, side):
            if node:
                if key > node.val:
                    tree_traversal(getattr(node, "right"), key, node, "right")
                elif key < node.val:
                    tree_traversal(getattr(node, "left"), key, node, "left")
                else:
                    # print(parent_node.val if parent_node else None, node.val)
                    check_del_type(node, parent_node, side)


        if root:
            if getattr(root, "right") == None and getattr(root, "left") == None:
                if key == root.val:
                    root = None
                    # print("afsadfdsafdsafsdafsad")
                    return root
            elif getattr(root, "left") == None:
                if key == root.val:
                    root = root.right
                    return root
            elif getattr(root, "right") == None:
                if key == root.val:
                    root = root.left
                    return root

        tree_traversal(root, key, root, None)


        return root
