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

def delete_node_from_linked_list(head: ListNode, position: int) -> ListNode:
    i = 1
    p = head
    if position == 1:
        head = p.next
    else:
        while p != None and i < position:
            i += 1
            q = p
            p = p.next
        q.next = p.next
    return head
    
    
class DLLNode:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
        
def get_all_list(head: DLLNode) -> list:
    result = []
    p = head
    while p != None:
        result.append(p.data)
        p = p.next
    return result

def get_length_of_linked_list(head: DLLNode) -> int:
    count = 0
    current = head
    while current:
        count += 1
        current = current.next
    return count

def DLLInsert(head: DLLNode, data: int, position: int):
    i = 1
    p = head
    new_node = DLLNode(data)
    if position == 1:
        new_node.next = p
        p.prev = new_node
        head = new_node
    else:
        while p != None and i < position:
            i += 1
            q = p
            p = p.next
        new_node.next = p
        new_node.prev = q
        q.next = new_node
        p.prev = new_node
        
    return head

def test_LL():
    # Here's a testcase of LL(Linked List)
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

    head = delete_node_from_linked_list(node1, 3)
    print(f'All list: {get_all_list(head)}')

def test_DLL():
    # Here's a testcase of DLL(Doubly Linked List)
    node1 = DLLNode(1)
    node2 = DLLNode(2)
    node3 = DLLNode(3)
    node4 = DLLNode(4)
    node5 = DLLNode(5)
    node6 = DLLNode(6)
    node1.next = node2
    node2.prev = node1
    node2.next = node3
    node3.prev = node2
    node3.next = node4
    node4.prev = node3
    node4.next = node5
    node5.prev = node4
    node5.next = node6
    print(f'List Length: {get_length_of_linked_list(node1)}')
    # print(node1.next)
    print(f'All lists: {get_all_list(node1)}')
    
    head = DLLInsert(node1, 4, 4)
    print(f'All lists: {get_all_list(head)}')

    # head = delete_node_from_linked_list(node1, 3)
    # print(f'All list: {get_all_list(head)}')

    
def main():
    # test_LL()
    test_DLL()
    
    
if __name__ == '__main__':
    main()