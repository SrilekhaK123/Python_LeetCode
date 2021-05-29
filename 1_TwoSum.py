def twoSum(nums, target):
    print(len(nums))
    list2=[]
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j] == target:
                list2.extend([i,j])
    print(list2)


twoSum([3,2,4], 6)
