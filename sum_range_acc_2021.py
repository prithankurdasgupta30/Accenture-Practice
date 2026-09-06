def calculate(m,n):
        sum = 0
        for i in range(m, n+1):
                if (i%3==0) and (i%5==0):
                        sum += i
        return sum
m, n = map(int, input().split())
print(calculate(m,n))