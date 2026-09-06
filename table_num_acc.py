def tableNum(n):
        sum = 0
        for i in range(1,11):
                value = n*i
                print(value,end=" ")
                sum = sum+value
        return sum
n = int(input())
print(tableNum(n))