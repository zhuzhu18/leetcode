# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def removeNthFromEnd(head, n: int):
    first_node = head
    hashMap = {}
    i = 0     # 节点数
    while head != None:
        hashMap[i] = head
        head = head.next
        i += 1
    deleteNode = hashMap[i-n]
    if i == n:
        return deleteNode.next
    hashMap[i-n-1].next = deleteNode.next
    del deleteNode
    return first_node

node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
node.next.next.next = ListNode(4)
node.next.next.next.next = ListNode(5)

a = removeNthFromEnd(node, 5)
while a != None:
    print(a.val)
    a = a.next