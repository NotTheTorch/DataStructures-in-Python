'''nums = [0,1,0,3,12]  # Output: [1,3,12,0,0]

low = 0


for high in range(len(nums)):
   if nums[high] != 0:
        nums[low], nums[high] = nums[high],nums[low]
        low += 1

print(nums)'''


"""nums = [0,1,0,3,12]
n = len(nums)
high = n - 1


for i in range(n):
    if nums[i] == 0:
        val = nums[i]
        nums.remove(val)
        nums.insert(high,val)

print(nums)"""


nums = [0,1,0,3,12]
n = len(nums)
res = [0] * n
index = 0

for i in range(n):
    if nums[i] != 0:
        res[index] = nums[i]
        index += 1

print(res)