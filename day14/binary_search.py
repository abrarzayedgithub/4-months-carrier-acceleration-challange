def binary_search(arr,target):
    low = 0
    high = len(arr) - 1
    while low<=high:
        mid_value = (low+high)//2
        if arr[mid_value] == target:
            return mid_value
        elif arr[mid_value] < target:
            low = mid_value + 1
        else:
            high = mid_value - 1

    return -1