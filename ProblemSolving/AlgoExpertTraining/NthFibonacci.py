#recursive solution Time O(2n) space O(N)
def getNthFib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return(getNthFib(n-1) + getNthFib(n-2))

#dynamic solution with memozation with recursion O(N) space | O(N) Time
def getNthFib(n, memoize = {1: 0, 2:1}):
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = getNthFib(n - 1, memoize) + getNthFib(n - 2, memoize)
        return memoize[n]