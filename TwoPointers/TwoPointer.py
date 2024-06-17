arr = [1,2,3,4,5]

onePointer = 0
twoPointer = len(arr)-1
targetValue = 9



while onePointer < twoPointer:
    sum = arr[onePointer]+arr[twoPointer]
    if sum == targetValue:
        print(True,onePointer,twoPointer)
        break

    elif sum < targetValue:
        onePointer += 1

    else:
        twoPointer -= 1


