def reverseLinkedList(head):
    current = head
    prev, next = None, None
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    head = prev
    return head