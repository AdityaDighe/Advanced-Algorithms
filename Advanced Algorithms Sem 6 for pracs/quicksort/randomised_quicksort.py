import random 

def quicksort(arr, start , stop, cost): 
    if start < stop: 
        pivotindex = partitionrand(arr, start, stop) 
        print("Pivot:", arr[pivotindex]) 
        print("Array after partitioning:", arr)
        quicksort(arr, start, pivotindex - 1, cost) 
        quicksort(arr, pivotindex + 1, stop, cost) 
    cost[0] += 1 

  

def partitionrand(arr, start, stop): 
    randpivot = random.randrange(start, stop) 
    arr[start], arr[randpivot] = arr[randpivot], arr[start] 
    return partition(arr, start, stop) 

  

def partition(arr, start, stop): 
    pivot = start 
    i = start + 1 
    for j in range(start + 1, stop + 1): 
        if arr[j] <= arr[pivot]: 
            arr[i], arr[j] = arr[j], arr[i] 
            i += 1 
    arr[pivot], arr[i - 1] = arr[i - 1], arr[pivot] 
    pivot = i - 1 
    return pivot 


array = [10, 7, 8, 9, 1, 5] 
print("Original array:", array) 
cost = [0] 
quicksort(array, 0, len(array) - 1, cost) 
print("Sorted array:", array) 
print("Total cost:", cost[0])
