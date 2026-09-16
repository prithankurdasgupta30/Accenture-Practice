import math
def standardDeviation(arr):
        total = 0
        for num in arr:
                total += num
        avg = total/len(arr)
        sqOfSum = 0
        for num in arr:
                sqOfSum += (num-avg)**2
        sd = math.sqrt(sqOfSum/len(arr))
        return sd
arr = list(map(int, input().split(",")))
print(standardDeviation(arr))