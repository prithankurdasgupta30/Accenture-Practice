def isPrime(n):
        if n<2:
                return False
        for i in range(2, int(n**0.5)+1):
                if n%i == 0:
                        return False
        return True
def digitSumPrime(n):
        total = 0
        while n>0:
                total += n%10
                n = n//10
        if isPrime(total):
                return "Yes"
        else:
                return "No"
n = int(input())
print(digitSumPrime(n))