def differenceOfSum(n,m):
        sum1, sum2 = 0, 0
        for i in range(1, m+1):
                if i%n == 0:
                        sum1 += i
                else:
                        sum2 += i
        return abs(sum1 - sum2)
n = int(input())
m = int(input())
print(differenceOfSum(n,m))