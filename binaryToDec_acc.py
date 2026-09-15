def binToDec(n):
        decimal = 0
        power = 0
        while n > 0:
                digit = n%10
                decimal += digit*(2**power)
                power += 1
                n = n//10
        return decimal
n = int(input())
print(binToDec(n))