def max_num(arr, n):
    max = arr[0]
    for x in range(0, n):
        if arr[x] > max:
            max = arr[x]
    return max


arr = [24, 22, 1, 12, 65, 2, 1, 4]
n = len(arr)
print(max_num(arr, n))
