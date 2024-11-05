class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next
    
def get_all_list(head: ListNode) -> list:
    result = []
    p = head
    while p != None:
        result.append(p.data)
        p = p.next
    return result

def get_length_of_linked_list(head: ListNode) -> int:
    count = 0
    current = head
    while current:
        count += 1
        current = current.next
    return count

def insert_in_linked_list(head: ListNode, data: int, position: int) -> ListNode:
    i = 1
    p = head
    new_node = ListNode(data)
    if position == 1:
        new_node.next = p
        head = new_node
    else:
        while p != None and i < position:
            i += 1
            q = p
            p = p.next
        q.next = new_node
        new_node.next = p
    return head

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
    print(f'List Length: {get_length_of_linked_list(node1)}')
    # print(node1.next)
    print(f'All lists: {get_all_list(node1)}')
    
    head = insert_in_linked_list(node1, 5, 10)
    print(f'All lists: {get_all_list(head)}')
    
if __name__ == '__main__':
    main()