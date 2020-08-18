# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def countNodes(root: TreeNode) -> int:
    if root == None:
        return 0
    else:
        return countNodes(root.left) + countNodes(root.right) + 1

p = TreeNode(10)
p.left = TreeNode(5)
p.right = TreeNode(15)

a = countNodes(p)
print(a)