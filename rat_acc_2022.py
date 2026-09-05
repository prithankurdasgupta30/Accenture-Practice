def calculate(r,unit,n,arr):
        if n == 0:
                return -1
        foodReq = r*unit
        foodGot = 0
        house = 0
        for house in range(n):
                foodGot += arr[house]
                if foodGot >= foodReq:
                        break
        if foodReq > foodGot:
                return 0
        return house + 1
r = int(input())
unit = int(input())
n = int(input())
arr = list(map(int, input().split()))
print(calculate(r,unit,n,arr))