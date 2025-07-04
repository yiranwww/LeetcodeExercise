# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop() # the last element
            if node:
                if visited:
                    res.append(node.val)
                # else: # pre-order: root -- left -- right
                #     stack.append((node.right, False))
                #     stack.append((node.left, False))
                #     stack.append((node, True))

                # else: # posterorder: left - right - root
                #     stack.append((node, True))
                #     stack.append((node.right, False))
                #     stack.append((node.left, False))

                else: # inorder: left - root - right
                    stack.append((node.right, False))
                    stack.append((node, True))
                    stack.append((node.left, False))
        return res
