def FindMissing(arr):
        n = len(arr)+1
        totalSum = (n*(n+1))//2
        actualSum = sum(arr)
        return totalSum - actualSum
arr = list(map(int, input().split()))
print(FindMissing(arr))