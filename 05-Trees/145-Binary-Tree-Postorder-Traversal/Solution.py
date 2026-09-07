# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root):
        result = []

        def dfs(node, result):
            if not node:
                return

            dfs(node.left, result)
            dfs(node.right, result)
            result.append(node.val)

        dfs(root, result)
        return result