class Node:
    def __init__(self, v):
        self.val = v
        self.next = None

def reverse(head: Node) -> Node:
    if head.next == None:
        return head
    next = head.next
    newHead = reverse(next)
    next.next = head
    head.next = None
    return newHead

node = Node(1)
node.next = Node(2)
node.next.next = Node(3)
node.next.next.next = Node(4)

node = reverse(node)
def output(node):
    while node != None:
        print(node.val)
        node = node.next
output(node)