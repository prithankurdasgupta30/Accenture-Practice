def vowelPer(s):
        con = 0
        for ch in s:
                if ch not in "AEIOUaeiou":
                        con += 1
        fact = 1
        for i in range(1, con+1):
                fact *= i
        return fact
s = input()
print(vowelPer(s))