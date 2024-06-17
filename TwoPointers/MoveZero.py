nums = [0,1,0,3,12]  # Output: [1,3,12,0,0]

low = 0


for high in range(len(nums)):
   if nums[high] != 0:
        nums[low], nums[high] = nums[high],nums[low]
        low += 1

print(nums)
