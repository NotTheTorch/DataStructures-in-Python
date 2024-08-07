def bubble_sort(arr,n):
    for i in range(n-1):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    
    return arr

num = 6
a = [13,20,9,24,46,52]
print(bubble_sort(a,num))