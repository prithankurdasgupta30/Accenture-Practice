def sumPrime(n):
        total = 0
        for num in range(2, n):
                isPrime = True
                for j in range(2, int(num**0.5)+1):
                        if num%j == 0:
                                isPrime = False
                                break
                if isPrime:
                        total += num
        return total
n = int(input())
print(sumPrime(n))