nums = [22,11,5,9,0,3,32]

nums.sort()

n = len(nums)
low = 0
high = n-1
mid = n //2

element = 9

while(True):
    if element > nums[mid]:
        low = mid + 1
        mid = (low + high)//2
    elif element < nums[mid]:
        high = mid - 1
        mid = (low + high)//2
    elif element == nums[mid]:
        print("Element Found:",element,"at position", mid)
        break


