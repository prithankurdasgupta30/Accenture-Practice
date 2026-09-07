def autoCount(n):
        count = [0]*10
        for digits in n:
                count[int(digits)] += 1
        for i in range(len(n)):
                if int(n[i]) != count[i]:
                        return 0
        return len(set(n))
n = input()
print(autoCount(n))