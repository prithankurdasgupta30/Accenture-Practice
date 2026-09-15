def repeatString(s,n):
        final = ""
        while n>0:
                final += s
                n -= 1
        return final
s = input()
n = int(input())
print(repeatString(s,n))