# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 1. The Roster: Instantly look up any employee's index
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        # 2. The Blueprint: Tracks who the next boss is
        self.pre_idx = 0
        
        def build(left, right):
            # Base Case: The team is empty
            if left > right:
                return None
            
            # Step A: The Blueprint tells us the current boss
            root_val = preorder[self.pre_idx]
            root = TreeNode(root_val)
            self.pre_idx += 1
            
            # Step B: Find the boss in the Roster to divide the teams
            mid = inorder_map[root_val]
            
            # Step C: Assign the remaining people to the left and right teams
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            
            return root
            
        # Start by handing the entire Roster to the function
        return build(0, len(inorder) - 1)