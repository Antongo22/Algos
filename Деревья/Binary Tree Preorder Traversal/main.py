from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def travel(self, node : Optional[TreeNode], res : List[int]):
        if node is None:
            return

        res.append(node.val)
        self.travel(node.left, res)
        self.travel(node.right, res)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.travel(root, res)
        return res
