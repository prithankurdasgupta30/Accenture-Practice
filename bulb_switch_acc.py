def bulbSwitch(arr, n):
        count = 0
        for i in range(n):
                if arr[i] == 0:
                        arr[i] = 1
                        for j in range(i+1, n):
                                arr[j] = 1 - arr[j]
                        count += 1
        return count
arr = list(map(int, input().split(",")))
n = len(arr)
print(bulbSwitch(arr,n))