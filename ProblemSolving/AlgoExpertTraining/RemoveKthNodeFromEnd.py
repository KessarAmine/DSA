class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    # Set a slow and fast pointer
    slow = fast = head
    # Move the fast pointer k steps ahead
    for i in range(k):
        fast = fast.next
    # If the fast pointer is already at the end, the head needs to be removed
    if not fast:
        head.value = head.next.value
        head.next = head.next.next
        return
    # Otherwise, move both pointers until the fast pointer reaches the end
    while fast.next:
        slow = slow.next
        fast = fast.next
    # Set the next value of the slow pointer to the next next value, effectively skipping the kth node
    slow.next = slow.next.next

#========================================================================================================================
def get_length(head):
    i = 0
    while head != None:
        head = head.next
        i += 1
    return i
    
def removeFirstNode(head):
    if not head:
        return None
    temp = head
    temp = None
    head = head.next
    return head

def removeKthNodeFromEnd(head, k):
    if head == None:
        return head
    index = get_length(head) - k
    i = 0
    temp = head
    prev = head
    if index == 0:
        prev = head.next
        temp = removeFirstNode(head)
    while temp != None:
        if i == index:
            prev.next = temp.next
            temp = prev
        i += 1
        prev = temp
        temp = temp.next
