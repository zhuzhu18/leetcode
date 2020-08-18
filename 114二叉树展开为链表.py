class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def flatten(root: TreeNode) -> None:
    if root == None:
        return
    if root.left == None and root.right == None:
        return
    left = root.left
    right = root.right
    flatten(right)
    flatten(left)
    if left != None:
        tmp = left
        while tmp.right != None:
            tmp = tmp.right
        tmp.right = root.right
        root.right = left
        root.left = None

node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(5)
node.left.left = TreeNode(3)
node.left.right = TreeNode(4)
node.right.right = TreeNode(6)
flatten(node)
while node:
    print(node.val)
    node = node.right