# To detect the loop we use floyd cycle detection, to finde the head we do arethmetic
# first = d + p
# second = 2d + 2p
# r = T - p - d
# T = 2d + p
# r = 2d + p - p - d 
# r = d
# SPACE O(1) | TIME O(N)
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def findLoop(head):
    first = head
    second = head
    while second.next is not None and first is not None and second is not None:
        first = first.next
        second = second.next.next
        if first == second:
            first = head
            while first is not second:
                first = first.next
                second = second.next
            break
    return first