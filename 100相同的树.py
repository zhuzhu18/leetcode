# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    if p == None and q != None:
        return False
    elif p != None and q == None:
        return False
    elif p == None and q == None:
        return True
    return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

p = TreeNode(10)
p.left = TreeNode(5)
p.right = TreeNode(15)
q = TreeNode(10)
q.left = TreeNode(5)
q.left.right = TreeNode(15)
a = isSameTree(p, q)
print(a)