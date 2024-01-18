# https://leetcode.com/problems/max-number-of-k-sum-pairs/?envType=study-plan-v2&envId=leetcode-75

nums = [3,1,3,4,3]
k = 6


nums.sort()
ops = 0
left = 0
right = len(nums)-1            

while left < right: 
    s = nums[left] + nums[right] 
    if s < k:
        left += 1 
    elif s > k: 
        right -= 1
    else: 
        ops += 1
        left += 1
        right -= 1

print(ops)