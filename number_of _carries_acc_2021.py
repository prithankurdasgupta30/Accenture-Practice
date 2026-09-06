def numberOfCarries(n1, n2):
        carry = 0
        count = 0
        if len(n1) <= len(n2):
                l = len(n1) - 1
        else:
                l = len(n2) - 1
        for i in range(l+1):
                temp = int(n1[l-i]) + int(n2[l-i]) + carry
                if len(str(temp)) > 1:
                        carry = 1
                        count += 1
                else:
                        carry = 0
        return count+carry
n = input()
m = input()
print(numberOfCarries(n, m))
        