def magicNum(n):
        count = 0
        for i in range(1, n+1):
                binary = bin(i)[2:]
                zeroCount = binary.count('0')
                if zeroCount % 2 == 1:
                        count += 1
        return count
n = int(input())
print(magicNum(n))