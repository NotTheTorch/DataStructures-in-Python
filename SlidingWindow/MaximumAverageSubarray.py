nums = [1,12,-5,-6,50,3]
k = 4
i = 0
sum = 0
maxValue = float('-inf')

while i < len(nums):
    sum += nums[i]
    
    if i >= k-1:
        maxValue = max(maxValue,sum)
        sum -= nums[i-(k-1)]
    i+=1

print(maxValue/k)