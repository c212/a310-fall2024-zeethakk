def quicksort(arr): #[3,6,8,10,1,2,1] first time, [3,6,8,1,2,1], [3,6,8,2], [3,6,2], [3,2], [3]
    if len(arr) <= 1:
        return arr #[3]
    pivot = arr[len(arr) // 2] #pivot = arr[3] = 10, pivot = arr[3] = 1, pivot = arr[2] = 8, pivot=arr[1]=6, pivot=arr[1]=2
    left = [x for x in arr if x < pivot] #left = [3,6,8,1,2,1], [], [3,6,2], [3,2], []
    middle = [x for x in arr if x == pivot] #middle = [10], [1,1], [8], [6], [2]
    right = [x for x in arr if x > pivot] #right = [], [3,6,8,2], [], [], [3]
    return quicksort(left) + middle + quicksort(right) #quicksort([3,6,8,1,2,1]) + [10] + [], [] + [1,1] + quicksort([3,6,8,2]) + [10], [1,1] + quicksort([3,6,2]) + [8] + [] + [10], [1,1] + quicksort([3,2]) + [6] + [] + [8,10], [1,1] + [] + [2] + quicksort([3]) + [6,8,10]

# Testing the quicksort function
arr = [3, 6, 8, 10, 1, 2, 1]
print(quicksort(arr))
#[1,1,2,3,6,8,10]