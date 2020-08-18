class TreeNode:
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None

node1 = TreeNode(5)     # 以node1为根开始构建一棵二叉搜索树
node1.left = TreeNode(3)
node1.left.left = TreeNode(1)
node1.left.left.right = TreeNode(2)
node1.left.right = TreeNode(4)
node1.right = TreeNode(6)

def inorder_traversal(root: TreeNode):
    arr = []
    stack = []
    while root is not None or len(stack) > 0:
        while root is not None:      # 一直循环遍历左子树, 到左子树为空为止
            stack.append(root)
            root = root.left
        if len(stack) > 0:     # 没有左儿子时从栈里弹出一个节点, 再以弹出节点的右儿子为根继续循环遍历它的左子树
            visit_node = stack.pop()
            arr.append(visit_node.val)
            root = visit_node.right
    return arr

def preorder_traversal(root):
    arr = []
    stack = []
    while root is not None or len(stack) > 0:
        while root is not None:
            arr.append(root.val)      # 遇到一个节点时先访问它, 再入栈, 以便弹出时找到它的右儿子
            stack.append(root)
            root = root.left
        if len(stack) > 0:
            tmp = stack.pop()
            root = tmp.right     # 开始处理右儿子为根的情况
    return arr

def postorder_traversal(root):
    arr = []
    stack = []
    pre_visited = None    # 定义一个前一次已访问过的节点
    while root is not None or len(stack) > 0:
        while root is not None:
            stack.append(root)
            root = root.left
        if len(stack) > 0:
            if stack[-1].right is None or stack[-1].right == pre_visited:
                tmp = stack.pop()
                pre_visited = tmp
                arr.append(tmp.val)
            else:
                root = stack[-1].right
    return arr
a = inorder_traversal(node1)    # 中序遍历
b = preorder_traversal(node1)    # 先序遍历
c = postorder_traversal(node1)    # 后序遍历
print(a)
print(b)
print(c)