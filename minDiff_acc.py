def findMinDiff(arr, m):
        n = len(arr)
        if n==0 or m==0 or m>n:
                return 0
        arr = sorted(arr)
        minDiff = float('inf')
        for i in range(n-m+1):
                diff = arr[i+m-1] - arr[i]
                minDiff = min(minDiff, diff)
                if diff < minDiff:
                        minDiff = diff
        return minDiff
arr = list(map(int, input().split()))
m = int(input())
print(findMinDiff(arr, m))
