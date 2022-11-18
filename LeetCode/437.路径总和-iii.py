#
# @lc app=leetcode.cn id=437 lang=python3
#
# [437] 路径总和 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res=0
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        self.dfs(root,targetSum)
        self.pathSum(root.left,targetSum)
        self.pathSum(root.right,targetSum)
        return self.res

    def dfs(self,root,target):
        if not root:
            return 
        target-=root.val
        if target==0:
            self.res+=1
        self.dfs(root.left,target)
        self.dfs(root.right,target)

# @lc code=end
