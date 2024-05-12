def partition(array, low, high, cost): 
    pivot = array[high] 
    i = low - 1 
    print("Pivot:", pivot) 
    for j in range(low, high): 
        if array[j] <= pivot: 
            i = i + 1 
            (array[i], array[j]) = (array[j], array[i]) 
    (array[i + 1], array[high]) = (array[high], array[i + 1]) 
    print("Array after partitioning:", array) 
    cost[0] += 1 
    return i + 1 

  

def quicksort(array, low, high, cost): 
    if low < high: 
        pi = partition(array, low, high, cost) 
        quicksort(array, low, pi - 1, cost) 
        quicksort(array, pi + 1, high, cost) 

  

if __name__ == '__main__': 
    array = [10, 7, 8, 9, 1, 5] 
    N = len(array) 
    print("Original array:", array) 
    cost = [0] 
    quicksort(array, 0, N - 1, cost) 
    print('Sorted array:') 
    for x in array: 
        print(x, end=" ") 
    print("\nTotal cost:", cost[0]) 