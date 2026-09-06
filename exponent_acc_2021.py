def countExp(i):
        count = 0
        while i%2 == 0 and i!=0:
                count +=1
                i = i//2
        return count
def maxExp(a,b):
        maximum, number = 0, a
        for i in range(a,b):
                temp = countExp(i)
                if temp > maximum:
                        maximum, number = temp, i
        return number
a, b = map(int, input().split())
print(maxExp(a,b))