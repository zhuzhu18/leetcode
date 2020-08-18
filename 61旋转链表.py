class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def rotateRight(head: ListNode, k: int):
    if head == None:
        return head
    old_head, old_tail = head, head
    nodes = 1
    while old_tail.next != None:
        old_tail = old_tail.next
        nodes += 1
    new_tail = old_head
    k = k % nodes
    tmp = nodes - k
    while tmp > 1:
        new_tail = new_tail.next
        tmp -= 1
    old_tail.next = old_head
    new_head = new_tail.next
    new_tail.next = None
    return new_head

node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
node.next.next.next = ListNode(4)
node.next.next.next.next = ListNode(5)
node = rotateRight(node, 2)
while node != None:
    print(node.val)
    node = node.next