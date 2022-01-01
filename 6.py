nums = [0,1,0,3,12]
for j in range(len(nums)-1):
    for i in range(len(nums)-1):
        n = nums[i]
        if n == 0:
            temp = nums[i+1]
            nums[i+1] = n
            nums[i] = temp
print(nums)
