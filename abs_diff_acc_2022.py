def findDiffCount(arr, n, num, diff):
        count = 0
        for i in range(n):
                if abs(arr[i] - num) <= diff:
                        count += 1
        if count:
                return count
        return 0
arr = list(map(int, input().split()))
n = len(arr)
num = int(input())
diff = int(input())
print(findDiffCount(arr, n, num, diff))