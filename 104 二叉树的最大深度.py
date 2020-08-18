# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
res = 0
def maxDepth(root: TreeNode):
    global res
    stack = []
    visited = None
    while root != None or len(stack) > 0:
        while root != None:
            stack.append(root)
            root = root.left

        if stack[-1].right != None and stack[-1].right != visited:
            root = stack[-1].right
        else:
            res = max(res, len(stack))
            visited = stack.pop()
    return res

node = TreeNode(3)
node.left = TreeNode(9)
node.right = TreeNode(20)
node.right.left = TreeNode(15)
node.right.right = TreeNode(7)

a = maxDepth(node)
print(a)