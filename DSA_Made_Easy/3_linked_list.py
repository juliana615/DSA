class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next
    

def get_list_length(head: ListNode) -> int:
    count = 0
    current = head
    while current:
        count += 1
        current = current.next
    return count

def main():
    # Here's a testcase
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    print(f'List Length: {get_list_length(node1)}')

if __name__ == '__main__':
    main()