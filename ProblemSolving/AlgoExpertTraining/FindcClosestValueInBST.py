#recursive approach where we create frames in the call stack
#Average : O(log(n)) time | O(log(n))  space
#Worst : O(n) time | O(n) space
def findClosestValueInBst(tree, target):
    return(helper(tree, target, float("inf")))

def helper(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    if target < tree.value:
        return helper(tree.left, target, closest)
    elif target > tree.value:
        return helper(tree.right, target, closest)
    else:
        return closest
# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
