def productSmallestPair(sum1, arr):
        n = len(arr)
        if n < 2:
                return -1
        arr = sorted(arr)
        for i in range(n - 1):
                if arr[i] + arr[i+1] < sum1:
                        return arr[i] * arr[i+1]
        return 0
sum1 = int(input())
arr = list(map(int, input().split()))
print(productSmallestPair(sum1, arr))