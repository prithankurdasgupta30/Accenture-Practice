def tran_sum(arr):
    totalSum = 0
    for i in range (len(arr)):
        longNum = (arr[i] - (i%7)*3)
        if (arr[i]%11 == 0):
            longNum += arr[i]//11
        totalSum += longNum
    return totalSum
arr = list(map(int, input().split()))
print(tran_sum(arr))