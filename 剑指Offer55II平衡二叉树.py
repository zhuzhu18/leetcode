# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.res = True
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if root == None:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        if abs(left-right) > 1:
            self.res = False
        return max(left, right) + 1

node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(2)
node.left.left = TreeNode(3)
node.left.right = TreeNode(3)
node.left.left.left = TreeNode(4)
node.left.left.right = TreeNode(4)

s = Solution()
a = s.isBalanced(node)
print(a)