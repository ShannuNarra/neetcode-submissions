# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):
            # Base Case: An empty space is always valid
            if not node:
                return True
                
            # Crash Test: Did the node step out of bounds?
            if not (left < node.val < right):
                return False
                
            # Pass the guardrails down to the left and right children
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)

        # Start the root with infinite guardrails
        return valid(root, float("-inf"), float("inf"))