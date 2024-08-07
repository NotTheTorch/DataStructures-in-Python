def insertion_sort(n,arr):
    for i in range(n-1):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    return arr

num = 7
a = [14,9,15,12,6,8,13]
print(insertion_sort(num,a))
