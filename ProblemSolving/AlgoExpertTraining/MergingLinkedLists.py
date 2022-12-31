class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def getIntersectionStart(linkedListOne, linkedListTwo):
    head1 = linkedListOne
    head2 = linkedListTwo
    start = None
    while head1 is not None:
        temp = head1
        current1 = head1.value
        while head2 is not None:
            if head2.value != current1:
                head2 = head2.next
            while head2 is not None and head1 is not None and head1.value == head2.value:
                if start == None:
                    start = head1
                head2 = head2.next
                head1 = head1.next
        head2 = linkedListTwo
        head1 = temp.next
    return start
    
def mergingLinkedLists(linkedListOne, linkedListTwo):
    intersection = getIntersectionStart(linkedListOne, linkedListTwo)
    return intersection
