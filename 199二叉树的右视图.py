class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def rightSideView(root: TreeNode) -> [int]:
    res = []
    if root == None:
        return res
    queue = []
    queue.append(root)
    while len(queue) > 0:
        size = len(queue)       # 当前队列的大小, 即当前层的节点数
        for i in range(size):
            visit_node = queue.pop(0)
            left = visit_node.left
            right = visit_node.right
            if left != None:
                queue.append(left)
            if right != None:
                queue.append(right)
            if i == size - 1:     # 遍历到当前层的最后一个节点时, 将当前层的最后一个节点的值存入结果中
                res.append(visit_node.val)
    return res

node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(3)
node.right.right = TreeNode(4)
node.left.right = TreeNode(5)
a = rightSideView(node)
print(a)