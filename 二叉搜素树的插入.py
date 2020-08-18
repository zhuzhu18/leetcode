class Node:
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None

def insert(tree:Node, v):    # 二叉搜索树插入的递归实现
    if tree == None:
        return Node(v)
    elif v <= tree.val:
        tree.left = insert(tree.left, v)
    else:
        tree.right = insert(tree.right, v)
    return tree

def insert2(tree, v):       # 二叉搜索树插入的非递归实现
    cur = tree
    parent = None
    while cur != None:
        parent = cur        # cur指向当前应该插入的位置, parent指向要插入节点位置的父节点
        if v <= cur.val:
            cur = cur.left
        else:
            cur = cur.right
    if parent == None:
        return Node(v)
    else:
        if v <= parent.val:
            parent.left = Node(v)
        else:
            parent.right = Node(v)
    return tree

def inorder(tree: Node):      # 二叉树的中序遍历
    res = []
    stack = []
    while tree != None or len(stack) > 0:
        while tree != None:
            stack.append(tree)
            tree = tree.left
        if len(stack) > 0:
            tmp = stack.pop()
            res.append(tmp.val)
            tree = tmp.right
    return res

tree = insert(None, 2)          # 元素插入的顺序不一样，得到的树结构不一样，但中序遍历结果是一样的，先序和后序结果可能不一样
tree = insert(tree, 1)
tree = insert(tree, 4)
tree = insert(tree, 5)
tree = insert(tree, 3)

a = inorder(tree)       # 二叉搜索树的中序遍历结果为从小到大排序
print(a)