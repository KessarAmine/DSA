#Space O(N) | TIME O(N)
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def Helper(root, somme, sums):
    if root is None:
        return
    somme += root.value
    if root.right is None and root.left is None:
        sums.append(somme)
        return 
    Helper(root.left, somme, sums)
    Helper(root.right, somme, sums)
    
def branchSums(root):
    sums = []
    Helper(root, 0, sums)
    return sums
