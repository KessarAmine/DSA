def Helper(root, level):
    if root is None:
        return 0
    return level + Helper(root.left, level + 1) + Helper(root.right, level + 1)
    
def nodeDepths(root):
    return Helper(root, 0)