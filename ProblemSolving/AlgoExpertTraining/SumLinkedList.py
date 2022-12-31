class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
        
    def insertTail(self, head, nodeToInsert):
        temp = head
        while temp.next is not None:
            temp = temp.next
        temp.next = nodeToInsert
        return head
        
def sumOfLinkedList(head):
    level = 0
    sum = 0
    while head is not None:
        current = head.value
        if level == 0:
            sum += current
        else:
            for i in range(0, level):
                current *= 10
            sum += current
        level += 1
        head = head.next
    return sum
    
def printFakeLinkedList(sum):
    result = None
    level = 1
    temp = sum
    while  sum / 10 > 1:
        current = temp % 10
        if level == 1:
            result = LinkedList(current)
        else:
            result = result.insertTail(result, LinkedList(int(current)))
        level *= 10
        sum /= 10
        temp /= 10
    if sum / 10 >= 0:
        current = temp % 10
        if result is None:
            result = LinkedList(current)
        else:
            result = result.insertTail(result, LinkedList(int(current)))
    return result
    
def sumOfLinkedLists(linkedListOne, linkedListTwo):
    sum1 = sumOfLinkedList(linkedListOne)
    sum2 = sumOfLinkedList(linkedListTwo)
    result = printFakeLinkedList(sum1 + sum2)
    return result
