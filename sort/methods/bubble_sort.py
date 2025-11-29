def BubbleSort(arr):
    n = len(arr)
    for i in range(1, n):
        for j in range(0, n-i):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = BubbleSort(arr)
    print("Sorted array is:", sorted_arr)