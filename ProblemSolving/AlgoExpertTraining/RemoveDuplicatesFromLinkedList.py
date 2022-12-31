class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    visited = []
    head = linkedList
    prev = linkedList
    while head != None:
        if head.value not in visited:
            visited.append(head.value)
        else:
            prev.next = head.next
            head = prev
        prev = head
        head = head.next
    return linkedList
