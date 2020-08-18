class Node:
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None
        self.count = 0

def countSmaller(nums: [int]) -> [int]:
    tree = None
    result = [0 for _ in range(len(nums))]
    for i in range(len(nums)-1, -1, -1):
        tree = insert(tree, nums[i], result, i)
    return result

def insert(tree, v, result, i):  # 二叉搜索树插入的非递归实现
    cur = tree
    parent = None
    while cur != None:
        parent = cur  # cur指向当前应该插入的位置, parent指向要插入节点位置的父节点
        if v <= cur.val:
            parent.count += 1
            cur = cur.left
        else:
            result[i] += parent.count + 1
            cur = cur.right
    if parent == None:
        return Node(v)
    else:
        if v <= parent.val:
            parent.left = Node(v)
        else:
            parent.right = Node(v)
    return tree

a = [21, 84, 66, 65, 36, 100, 41]
b = countSmaller(a)
print(b)