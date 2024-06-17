nums = [-4,-1,0,3,10]
n = len(nums)
res = [0]  * n
l,r = 0, n-1

for i in range(n-1,-1,-1):
    if abs(nums[l]) > abs(nums[r]):
        val = nums[l]
        l += 1
    else:
        val = nums[r]
        r -= 1
    
    res[i] = val ** 2

print(res)
