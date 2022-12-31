def getStart(nums, num):
    for i in range(0, len(nums)):
        if nums[i] == num:
            return i
			
def zeroSumSubarray(nums):
    sums = []
    for i in range(0, len(nums)):
        print(sums)
        if not len(sums):
            sums.append(nums[i])
        else:
            newelem = sums[len(sums) - 1] + nums[i]
            if newelem == 0:
                return True
            if newelem not in sums:
                sums.append(newelem)
            else:
                start = getStart(nums, newelem)
                print(nums[start:i])
                return True
    if sum(sums) == 0 and len(sums):
        return True
    return False
