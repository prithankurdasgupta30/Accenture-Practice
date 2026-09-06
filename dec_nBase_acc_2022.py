def dectoNBase(n, num):
        remainder = []
        q = num//n
        remainder.append(num%n)
        while q!=0:
                remainder.append(q%n)
                q = q//n
        remainder = remainder[::-1]
        equivalent = ""
        for i in remainder:
                if i > 9:
                        a = i-9
                        a = 64+a
                        equivalent += chr(a)
                else:
                        equivalent += str(i)
        return equivalent
n = int(input())
num = int(input())
print(dectoNBase(n, num))