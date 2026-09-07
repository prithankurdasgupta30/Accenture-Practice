def maxInArray(arr, n):
        max_val = arr[0]
        max_index = 0
        for i in range(1,n):
                if arr[i] > max_val:
                        max_val = arr[i]
                        max_index = i
        print(max_val)
        print(max_index)
arr = list(map(int, input().split()))
n = len(arr)
maxInArray(arr, n)