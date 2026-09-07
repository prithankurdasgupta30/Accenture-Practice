def checkPal(n,m):
        for i in range(n, m+1):
                rev = 0
                temp = i
                while temp != 0:
                        remainder = temp%10
                        rev = rev*10 + remainder
                        temp = temp // 10
                if rev == i:
                        print(i, end=" ")
        return -1
n = int(input())
m = int(input())
checkPal(n,m)