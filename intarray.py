nums = [1, 2, 3, 4]

def DistinctCheck(nums):
    distinct = 0
    for n in range(len(nums)):
        for y in range(len(nums)):
            if nums[n] == nums[y] & n != y:
                distinct += 1
    
    if distinct == 0:
        return False
    else:
        return True

print(DistinctCheck(nums))

def ListCheck(nums):
    return False if nums == list(dict.fromkeys(nums)) else True

print(ListCheck(nums))