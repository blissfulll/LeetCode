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
        def node_del(root_node, del_node, parent_node, node):

            # if not node:
            #     return

            # print("AAAAAA")
            # if not node:
            #     # print(parent_node.val, "BBBBB")
                
            #     root_node.left = parent_node
            #     parent_node.right = getattr(node, "left", None)
            #     return

            if hasattr(node, "right") and node.right != None:
                node_del(root_node, del_node, node, node.right)
            else:
                # print(parent_node.val, "BBBBB")
                if parent_node == del_node:
                    node.right = getattr(del_node, "right")
                    root_node.left = node
                else:

                    if hasattr(node, "left"):
                        parent_node.right = node.left
                        node.left = None
                    node.right = getattr(del_node, "right")
                    node.left = del_node.left 
                    root_node.left = node
                    # if del_node.left != node else None
                    if root_node == del_node:
                        print(node.val)
                        root_node = node
                    # parent_node.right = getattr(node, "left", None)
                
        def check_del_type(node, parent_node, side):
            if getattr(node, "right") != None and getattr(node, "left") != None:
                # print(node.val, "FFFFF", parent_node.val)
                # node_del(node.left, node, node, parent_node)
                node_del(parent_node, node, node, node.left)
            elif getattr(node, "right"):
                # type2_del(node, parent_node, "right", side)
                setattr(parent_node, side, node.right)
            elif getattr(node, "left"):
                # type2_del(node, parent_node, "left", side)
                setattr(parent_node, side, node.leftt)
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


        tree_traversal(root, key, root, None)


        return root






















































        
        # def check_compat(node, side):
        #     if not node: return False
        #     return False if hasattr(node, side) and getattr(node, side) != None else True

        # def has_no_child(node):
        #     if node and not node.left  and not node.right:
        #         return True
        #     return False

        # def has_no_right_child(node):
        #     if node and not node.right:
        #         return True
        #     return False

        # def has_no_left_child(node):
        #     if node and not node.left:
        #         return True
        #     return False

        # def last_chance_left(node):
        #     if hasattr(node, "right") and hasattr(node.right, "right") and has_no_child(node.right.right):
        #         tmp = node.right.right
        #         node.right.right = None
        #         return tmp
        #     if hasattr(node, "right") and not has_no_child(node.right):
        #         last_chance_left(node.right)
        #     return None

        # def last_chance_right(node):
        #     if hasattr(node, "left") and hasattr(node.left, "left") and has_no_child(node.left.left):
        #         tmp = node.left.left
        #         node.left.left = None
        #         return tmp
        #     elif hasattr(node, "left") and not has_no_child(node.left):
        #         last_chance_right(node.left)
        #     return None

        # # def check_mid(node):
        # #     if hasattr(node, "left") and hasattr(node, "right"):
        # #         if hasattr(node.left, "right") and has_no_child(node.left.right):

        
        # def get_new_node(node):
        #     if hasattr(node, "left"):
        #         if hasattr(node, "right"):
        #             # check__left_right = last_chance_right(node.left)
        #             # if check__left_right:
        #             #     return check__left_right
        #             # check__right_left = last_chance_left(node.right)
        #             # if check__right_left:
        #             #     return check__right_left
        #             if hasattr(node.left, "right") and has_no_child(node.left.right):
        #                 tmp = node.left.right
        #                 node.left.right = None
        #                 tmp.right = node.right
        #                 tmp.left = node.left
        #                 # print("LR")
        #                 return tmp
        #             elif hasattr(node.right, "left") and has_no_child(node.right.left):
        #                 tmp = node.right.left
        #                 node.right.left = None
        #                 tmp.left = node.left
        #                 tmp.right = node.right
        #                 return tmp
        #             elif hasattr(node.left, "right") and has_no_right_child(node.left.right):
        #                 tmp = node.left.right
        #                 node.left.right = tmp.left
        #                 tmp.left = node.left
        #                 tmp.right = node.right
        #                 return tmp
        #             elif hasattr(node.right, "left") and has_no_left_child(node.right.left):
        #                 tmp = node.right.left
        #                 node.right.left = tmp.right
        #                 tmp.right = node.right
        #                 tmp.left = node.left
        #                 return tmp
        #             elif hasattr(node.left, "right") and hasattr(node.left.right, "right") and has_no_child(node.left.right.right):
        #                 tmp = node.left.right.right
        #                 node.left.right.right = None
        #                 tmp.left = node.left
        #                 tmp.right = node.right
        #                 return tmp
        #             elif hasattr(node.right, "left") and hasattr(node.right.left, "left") and has_no_child(node.right.left.left):
        #                 tmp = node.right.left.left
        #                 node.right.left.left= None
        #                 tmp.left = node.left
        #                 tmp.right = node.right
        #                 return tmp
        #             elif check_compat(node.left, "right"):
        #                 node.left.right = node.right
        #                 # print("LR")
        #                 return node.left 
        #             elif check_compat(node.right, "left"):
        #                 node.right.left = node.left
        #                 # print("RL")
        #                 return node.right
        #             else:
        #                 print("AAAAAAAAAA")
        #                 # print(node.val, node.right.val, node.left.val)
        #                 return node.right
        #         else:
        #             return node.left

        #     elif hasattr(node, "right"):
        #         return node.right

        #     return None

        # def dfsRec(node):

        #     if key < node.val:
        #         if hasattr(node, "left") and node.left:
        #             if node.left.val == key:
        #                 # print("AAA")
        #                 node.left = get_new_node(node.left)
        #                 return
        #             else:
        #                 dfsRec(node.left)

        #     elif key > node.val:

        #         if hasattr(node, "right") and node.right:
        #             if node.right.val == key:
        #                 # print("BBB")
        #                 node.right = get_new_node(node.right)
        #                 return
        #             else:
        #                 dfsRec(node.right)
        #     else:
        #         return


        # if not root:
        #     return None

        # if root.val == key:
        #     root = get_new_node(root)
        # else:
        #     dfsRec(root)
        
        # return root
